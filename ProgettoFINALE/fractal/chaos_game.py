# Samuel Panetto, Riccardo Gioia, Lorenzo Stagno - 4C INFO Sierpinski

import os
import random
import numpy as np
import matplotlib
# Usiamo 'Agg' per creare le immagini in background senza doverle aprire a schermo sul PC
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Funzione per decidere dove mettere i punti principali (gli angoli) della figura
def genera_vertici(numero_lati, raggio=1.0):
    vertici = []
    # Spostiamo tutto di 90 gradi così la punta della figura guarda verso l'alto
    offset = np.pi / 2 
    for i in range(numero_lati):
        # Dividiamo il cerchio in base a quanti lati vogliamo
        angolo = 2 * np.pi * i / numero_lati + offset
        # Troviamo le coordinate X e Y di ogni angolo usando seno e coseno
        vertici.append((raggio * np.cos(angolo), raggio * np.sin(angolo)))
    return np.array(vertici)

# Funzione principale che crea il frattale con il gioco del caos
def genera_frattale(num_vertici=3, distanza=0.5, iterazioni=30000,
                    scarta=100, colore="green", cartella_output="static/generated"):
    
    # Se la cartella per salvare le foto non esiste, il computer la crea in automatico
    os.makedirs(cartella_output, exist_ok=True)
    
    # Prendiamo le coordinate degli angoli calcolate prima
    vertici = genera_vertici(num_vertici)
    
    # Iniziamo a disegnare partendo dal centro esatto del grafico
    punto_corrente = np.array([0.0, 0.0])
    punti = []

    # Ripetiamo il calcolo per quante volte ha scelto l'utente (le iterazioni)
    for i in range(iterazioni):
        # Scegliamo un angolo a caso tra quelli della figura
        vertice_casuale = random.choice(vertici)
        
        # Facciamo saltare il punto verso l'angolo scelto usando la variabile distanza
        punto_corrente = (1 - distanza) * punto_corrente + distanza * vertice_casuale
        
        # Saltiamo i primi 100 punti per evitare che il disegno venga sporco all'inizio
        if i >= scarta:
            punti.append(punto_corrente.copy())

    # Trasformiamo i dati in un formato che la libreria grafica legge meglio
    punti = np.array(punti)
    
    # Diamo un nome unico al file così non cancelliamo le vecchie immagini nell'archivio
    nome_file = f"frattale_{random.randint(100000, 999999)}.png"
    percorso_file = os.path.join(cartella_output, nome_file)

    # Creiamo l'immagine vera e propria
    fig = plt.figure(figsize=(10, 10))
    
    # Usiamo un grigio scuro per lo sfondo dell'immagine per staccare dal nero del sito
    colore_sfondo_img = '#2c2c3e' 
    fig.patch.set_facecolor(colore_sfondo_img) 
    ax = plt.gca()
    ax.set_facecolor(colore_sfondo_img)

    # Colleghiamo i nomi dei colori ai codici neon per farli brillare di più
    colori_mappa = {
        "green": "#00ff9d",
        "blue": "#00e5ff",
        "red": "#ff5252",
        "purple": "#d500f9",
        "black": "#ffffff" # Il nero diventa bianco per risaltare sullo sfondo scuro
    }
    colore_finale = colori_mappa.get(colore, colore)

    # Disegniamo tutti i punti calcolati (s è la grandezza del puntino)
    plt.scatter(punti[:, 0], punti[:, 1], s=0.8, c=colore_finale, alpha=1.0, edgecolors='none', marker='.')
    
    # Mettiamo una griglia leggera per dare un tocco tecnico al grafico
    plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='#4a4a6a', alpha=0.6)
    
    # Cambiamo il colore dei numeri sui bordi per farli leggere bene sullo scuro
    ax.tick_params(axis='x', colors='#cccccc', labelsize=10)
    ax.tick_params(axis='y', colors='#cccccc', labelsize=10)

    # Togliamo i bordi sopra e a destra per rendere l'immagine più pulita
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#555577')
    ax.spines['bottom'].set_color('#555577')

    # Blocchiamo le proporzioni per non schiacciare la figura
    plt.axis("equal")

    # Salviamo l'immagine finale sul computer
    plt.savefig(percorso_file, dpi=300, bbox_inches="tight", pad_inches=0.2, facecolor=fig.get_facecolor())
    plt.close() # Chiudiamo tutto per non occupare troppa memoria
    
    return nome_file
