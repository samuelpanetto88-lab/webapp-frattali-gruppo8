# Web App sui Frattali

## Componenti del gruppo
- **Samuel Panetto** — backend, integrazione del server Flask, gestione delle route e collegamento tra frontend e generazione del frattale
- **Gioia Riccardo** — sviluppo Python, logica matematica e generazione del frattale
- **Lorenzo Stagno** — frontend, struttura delle pagine HTML, stile CSS e presentazione grafica del sito

## Descrizione del progetto
Questo progetto consiste nella realizzazione di una **web app interattiva sui frattali**, sviluppata nell’ambito di un lavoro scolastico multidisciplinare tra informatica e matematica.

L’applicazione ha l’obiettivo di:
- spiegare in modo chiaro che cosa sono i frattali;
- approfondire il **Triangolo di Sierpinski**, frattale assegnato al gruppo;
- permettere all’utente di generare immagini frattali in modo interattivo;
- salvare e mostrare le immagini create all’interno di un archivio consultabile.

Il progetto unisce quindi:
- una parte **teorica e matematica**, relativa alla geometria frattale e all’autosimilarità;
- una parte **informatica**, relativa alla costruzione di una vera applicazione web con server Python, interfaccia frontend e generazione di immagini.

---

## Obiettivi principali
La web app è stata progettata per soddisfare questi obiettivi:

1. presentare una spiegazione generale dei frattali;
2. dedicare una sezione specifica al **Triangolo di Sierpinski**;
3. permettere la generazione di frattali tramite parametri scelti dall’utente;
4. mostrare all’utente valori consigliati per ottenere immagini più nette e significative;
5. archiviare le immagini generate e renderle scaricabili in formato PNG;
6. documentare il lavoro di gruppo attraverso GitHub, con cronologia delle modifiche e contributi dei membri.

---

## Struttura della web app
La web app è organizzata in quattro sezioni principali:

### 1. Home
Pagina introduttiva che spiega:
- che cosa sono i frattali;
- il concetto di iterazione;
- l’autosimilarità;
- il rapporto tra matematica, natura e rappresentazione grafica.

### 2. Triangolo di Sierpinski
Pagina dedicata al frattale del gruppo, con:
- spiegazione del Triangolo di Sierpinski;
- descrizione del metodo del **Chaos Game**;
- formula utilizzata per generare i nuovi punti;
- indicazioni sui valori consigliati per ottenere figure più precise.

### 3. Il mio frattale
Sezione interattiva in cui l’utente può:
- scegliere il numero di vertici;
- impostare il rapporto di distanza `r`;
- scegliere il numero di iterazioni;
- scegliere il colore del frattale;
- generare un’immagine personalizzata.

La pagina include anche suggerimenti pratici sui valori da usare per evitare risultati poco leggibili.

### 4. Archivio
Pagina che raccoglie le immagini frattali generate e permette di:
- visualizzarle;
- scaricarle in formato PNG.

---

## Tecnologie utilizzate
Per la realizzazione del progetto sono state utilizzate le seguenti tecnologie:

- **Python** per la logica del progetto e la generazione del frattale
- **Flask** come framework backend per il server web
- **HTML** per la struttura delle pagine
- **CSS** per lo stile e il layout dell’interfaccia
- **Matplotlib** per il disegno e il salvataggio delle immagini frattali
- **NumPy** per la gestione dei calcoli matematici
- **GitHub** per il versionamento del progetto e la collaborazione di gruppo

---

## Struttura delle cartelle
Il progetto è organizzato in questo modo:

```text
progetto-frattale/
│
├─ app.py
├─ requirements.txt
├─ README.md
│
├─ fractal/
│  └─ chaos_game.py
│
├─ templates/
│  ├─ base.html
│  ├─ index.html
│  ├─ frattale.html
│  ├─ generatore.html
│  └─ archivio.html
│
└─ static/
   ├─ css/
   │  └─ style.css
   ├─ generated/
   ├─ icons/
   └─ manifest.json
