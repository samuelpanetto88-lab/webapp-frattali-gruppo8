from flask import Flask, render_template, request
from fractal.chaos_game import genera_frattale
import os

app = Flask(__name__)


# Uso una variabile globale per gestire light e dark mode del sito web
web_mode = None
def update_web_mode(request):
    # Recupero la variabile globale web_mode
    global web_mode
    # Controllo che sia stata effettuata una operazione di tipo POST
    if request.method  == "POST":
        # Controllo che il parametro mode sia stato inizializzato correttamente
        if request.form.get("mode") != None:
            # Assegno la nuova mode alla variabile globale
            web_mode = request.form.get("mode")


@app.route("/", methods=["GET", "POST"])
def home():
    update_web_mode(request=request)

    return render_template("index.html", web_mode=web_mode)


@app.route("/frattale", methods=["GET", "POST"])
def frattale():
    update_web_mode(request=request)

    return render_template("frattale.html", web_mode=web_mode)


@app.route("/generatore", methods=["GET", "POST"])
def generatore():
    immagine = None
    errore = None

    update_web_mode(request=request)

    if request.method == "POST":
        try:
            num_vertici = int(request.form.get("num_vertici", 3))
            distanza = float(request.form.get("distanza", 0.5))
            iterazioni = int(request.form.get("iterazioni", 30000))
            colore = request.form.get("colore", "green")

            nome_file = genera_frattale(
                num_vertici=num_vertici,
                distanza=distanza,
                iterazioni=iterazioni,
                scarta=100,
                colore=colore
            )

            immagine = f"generated/{nome_file}"

        except Exception as e:
            errore = str(e)

    return render_template("generatore.html", immagine=immagine, errore=errore, web_mode=web_mode)


@app.route("/archivio", methods=["GET", "POST"])
def archivio():
    update_web_mode(request=request)

    cartella = os.path.join("static", "generated")
    os.makedirs(cartella, exist_ok=True)

    files = sorted(os.listdir(cartella), reverse=True)
    immagini = [f"generated/{file}" for file in files if file.lower().endswith(".png")]

    return render_template("archivio.html", immagini=immagini, web_mode=web_mode)


if __name__ == "__main__":
    app.run(debug=True)