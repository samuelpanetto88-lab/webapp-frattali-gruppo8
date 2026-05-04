from flask import Flask, render_template, request
from fractal.chaos_game import genera_frattale
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/frattale")
def frattale():
    return render_template("frattale.html")


@app.route("/generatore", methods=["GET", "POST"])
def generatore():
    immagine = None
    errore = None

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

    return render_template("generatore.html", immagine=immagine, errore=errore)


@app.route("/archivio")
def archivio():
    cartella = os.path.join("static", "generated")
    os.makedirs(cartella, exist_ok=True)

    files = sorted(os.listdir(cartella), reverse=True)
    immagini = [f"generated/{file}" for file in files if file.lower().endswith(".png")]

    return render_template("archivio.html", immagini=immagini)


if __name__ == "__main__":
    app.run(debug=True)