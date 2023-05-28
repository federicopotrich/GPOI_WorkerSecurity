import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Leggi i dati dal file CSV
data = pd.read_csv("dati.csv")

# Crea un DataFrame pandas
df = pd.DataFrame(data)

# Definisci il nome delle colonne dei dati numerici (escludendo la colonna '#')
numeric_columns = df.columns[2:]

# Dizionario per le etichette personalizzate dei paesi
country_labels = {
    'IT': 'Italy',
    'BE': 'Belgium',
    'DE': 'Germany',
    'FR': 'France',
    'ES': 'Spain',
    'PL': 'Poland',
    'NL': 'Netherlands',
    'SE': 'Sweden',
    'AT': 'Austria',
    'RO': 'Romania'
}

selected_countries = list(country_labels.keys())

# Filtra i dati selezionati
df_selected = df.loc[df['geo_TIME_PERIOD'].isin(selected_countries)]

# Crea una figura e un'asse con dimensioni personalizzate
fig, ax = plt.subplots(figsize=(15, 8.8))

# Variabile per tenere traccia del frame corrente
current_frame = 0

# Lista dei colori (escludendo il bianco)
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'brown', 'cyan', 'magenta']

# Funzione di aggiornamento chiamata ad ogni frame dell'animazione
def update(frame):
    ax.clear()
    country_codes = df_selected['geo_TIME_PERIOD'].replace(country_labels)
    ax.bar(country_codes, df_selected[numeric_columns[frame]], color=colors[frame % len(colors)])
    ax.set_xticklabels(country_codes, rotation=90)
    ax.set_ylabel('Dati')
    ax.set_title('Contract Worker Security', fontweight='bold', fontsize=16)  # Aggiungi il titolo in italiano
    ax.legend([numeric_columns[frame]], loc='upper right')  # Aggiungi la legenda

# Funzione per gestire il click del mouse
def on_click(event):
    global current_frame
    if event.button == 1:  # Click sinistro del mouse
        current_frame = (current_frame + 1) % len(numeric_columns)
        update(current_frame)
        plt.draw()

# Aggiungi il gestore dell'evento click del mouse
fig.canvas.mpl_connect('button_press_event', on_click)

# Crea l'animazione iniziale
update(current_frame)

# Mostra l'animazione
plt.show()
