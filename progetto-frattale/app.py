from flask import Flask, render_template, request #flask crea l'istanza dell'applicazione, render_template per mostrare le pagine html e request per gestire i dati inviati dai form
from fractal.chaos_game import genera_frattale
import os

app = Flask(__name__)


@app.route("/")             #indirizzamento per la home page
def home():
    return render_template("index.html")


@app.route("/frattale")     #indirizzamento per la pagina del frattale
def frattale():
    return render_template("frattale.html")


@app.route("/generatore", methods=["GET", "POST"])   #indirizzamento per la pagina del generatore
def generatore():
    immagine = None
    errore = None
    num_vertici = 3
    distanza = 0.50
    iterazioni = 100000
    colore = "black"

    if request.method == "POST":
        try:
            num_vertici = int(request.form.get("num_vertici", num_vertici))
            distanza = float(request.form.get("distanza", distanza))
            iterazioni = int(request.form.get("iterazioni", iterazioni))
            colore = request.form.get("colore", colore)

            nome_file = genera_frattale(
                num_vertici=num_vertici,
                distanza=distanza,
                iterazioni=iterazioni,
                scarta=1000,                
                colore=colore
            )

            immagine = f"generated/{nome_file}"

        except Exception as e:      #converte lerrore in stringa e lo passa alla pagina html 
            errore = str(e)

    return render_template(
        "generatore.html",
        immagine=immagine,
        errore=errore,
        num_vertici=num_vertici,
        distanza=distanza,
        iterazioni=iterazioni,
        colore=colore,
    )


@app.route("/archivio")    #indirizzamento per la pagina dell archivio con tutte le immagini generate  
def archivio():
    cartella = os.path.join("static", "generated")
    os.makedirs(cartella, exist_ok=True)

    files = sorted(os.listdir(cartella), reverse=True)
    immagini = [f"generated/{file}" for file in files if file.lower().endswith(".png")]

    return render_template("archivio.html", immagini=immagini)


if __name__ == "__main__":      # verifica se il file è eseguito direttamente e in tal caso avvia l'applicazione Flask
    app.run(debug=True)     #avvia l'applicazione Flask in modalità debug necessario per lo sviluppo e tolto in produzione


# __name__ === "__main__" è una convenzione in Python che indica che il codice all'interno di questo blocco verrà eseguito
#  solo se il file viene eseguito direttamente, e non quando viene importato come modulo in un altro file. 
# In questo caso, se app.py viene eseguito direttamente, l'applicazione Flask verrà avviata. 
# Se invece app.py viene importato in un altro file, il codice all'interno di questo blocco non verrà eseguito, 
# evitando così di avviare l'applicazione Flask in modo indesiderato.
