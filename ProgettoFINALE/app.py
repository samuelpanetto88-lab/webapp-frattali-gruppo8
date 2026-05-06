# Samuel Panetto, Riccardo Gioia, Lorenzo Stagno - 4C INFO Sierpinski

from flask import Flask, render_template, request, redirect, url_for
from fractal.chaos_game import genera_frattale
import os

app = Flask(__name__)

# Pagina principale che carica il file index.html
@app.route("/")
def home():
    return render_template("index.html")

# Pagina dedicata alla spiegazione teorica del triangolo di Sierpinski
@app.route("/frattale")
def frattale():
    return render_template("frattale.html")

# Pagina del generatore: gestisce sia la visualizzazione che l'invio dei dati dal form
@app.route("/generatore", methods=["GET", "POST"])
def generatore():
    immagine = None
    errore = None
    
    # Se l'utente preme il tasto "Genera" (metodo POST)
    if request.method == "POST":
        try:
            # Recuperiamo i parametri inseriti dall'utente nel form
            num_vertici = int(request.form.get("num_vertici", 3))
            distanza = float(request.form.get("distanza", 0.5))
            iterazioni = int(request.form.get("iterazioni", 30000))
            colore = request.form.get("colore", "green")

            # Chiamiamo la funzione matematica per creare il file dell'immagine
            nome_file = genera_frattale(
                num_vertici=num_vertici,
                distanza=distanza,
                iterazioni=iterazioni,
                scarta=100,
                colore=colore
            )
            # Salviamo il percorso dell'immagine per mostrarla nella pagina
            immagine = f"generated/{nome_file}"
            
        except Exception as e:
            # Se qualcosa va storto (es. dati sbagliati), salviamo il messaggio di errore
            errore = str(e)
            
    return render_template("generatore.html", immagine=immagine, errore=errore)

# Pagina dell'archivio: legge tutti i file salvati nella cartella generated
@app.route("/archivio")
def archivio():
    # Creiamo il percorso della cartella dove salviamo i frattali
    cartella = os.path.join("static", "generated")
    # Se la cartella non esiste, la creiamo per evitare errori
    os.makedirs(cartella, exist_ok=True)
    
    # Prendiamo la lista dei file, mettendoli dal più recente al più vecchio
    files = sorted(os.listdir(cartella), reverse=True)
    # Creiamo una lista di percorsi completi solo per le immagini .png
    immagini = [f"generated/{file}" for file in files if file.lower().endswith(".png")]
    
    return render_template("archivio.html", immagini=immagini)

# Rotta per eliminare un singolo frattale dall'archivio
@app.route("/elimina/<path:img_path>")
def elimina_frattale(img_path):
    try:
        # Troviamo il percorso esatto del file nel computer
        percorso_pieno = os.path.join(app.root_path, 'static', img_path)
        # Se il file esiste davvero, lo cancelliamo fisicamente
        if os.path.exists(percorso_pieno):
            os.remove(percorso_pieno)
    except Exception as e:
        # Se c'è un errore (es. file già rimosso), lo scriviamo nel terminale
        print(f"Errore eliminazione: {e}")
    
    # Dopo aver eliminato, ricarichiamo la pagina dell'archivio
    return redirect(url_for('archivio'))

# Avvio del server in modalità debug per vedere le modifiche in tempo reale
if __name__ == "__main__":
    app.run(debug=True)
