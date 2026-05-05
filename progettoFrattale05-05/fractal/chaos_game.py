import os
import random
import uuid
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def genera_vertici(numero_lati, raggio=1.0):
    vertici = []

    for i in range(numero_lati):
        angolo = 2 * np.pi * i / numero_lati
        x = raggio * np.cos(angolo)
        y = raggio * np.sin(angolo)
        vertici.append((x, y))

    return np.array(vertici)


def genera_frattale(num_vertici=3, distanza=0.5, iterazioni=30000,
                    scarta=100, colore="green", cartella_output="static/generated"):
    if num_vertici < 3 or num_vertici > 12:
        raise ValueError("Il numero di vertici deve essere compreso tra 3 e 12.")

    if num_vertici == 4:
        raise ValueError("Con 4 vertici questa configurazione non produce un frattale significativo. Scegli 3, 5, 6 o altri valori.")

    if distanza < 0.10 or distanza > 0.90:
        raise ValueError("Il valore di r deve essere compreso tra 0.10 e 0.90.")

    if iterazioni < 1000 or iterazioni > 200000:
        raise ValueError("Il numero di iterazioni deve essere compreso tra 1000 e 200000.")

    os.makedirs(cartella_output, exist_ok=True)

    vertici = genera_vertici(num_vertici)
    punto_corrente = np.array([0.0, 0.0])
    punti = []

    for i in range(iterazioni):
        vertice_casuale = random.choice(vertici)
        punto_corrente = (1 - distanza) * punto_corrente + distanza * vertice_casuale

        if i >= scarta:
            punti.append(punto_corrente.copy())

    punti = np.array(punti)

    nome_file = f"frattale_{num_vertici}v_{uuid.uuid4().hex[:8]}.png"
    percorso_file = os.path.join(cartella_output, nome_file)

    plt.figure(figsize=(8, 8))
    plt.scatter(punti[:, 0], punti[:, 1], s=0.2, c=colore, alpha=0.8)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(percorso_file, dpi=300, bbox_inches="tight", pad_inches=0.1)
    plt.close()

    return nome_file