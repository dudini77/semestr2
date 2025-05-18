import networkx as nx
import matplotlib.pyplot as plt
import random
import os
import imageio

# Rysowanie grafu z agentem
def rysuj_graf(G, pozycje, agent_pos, krok, folder='frames'):
    plt.figure(figsize=(8, 6))
    kolory = ['red' if n == agent_pos else 'skyblue' for n in G.nodes()]
    nx.draw(G, pos=pozycje, with_labels=True, node_color=kolory, node_size=500)
    plt.title(f"Krok {krok}")
    plt.axis('off')

    if not os.path.exists(folder):
        os.makedirs(folder)

    sciezka = f"{folder}/frame_{krok:03d}.png"
    plt.savefig(sciezka)
    plt.close()

# Tworzenie animacji gif
def stworz_animacje(folder='frames', wyjscie='animacja.gif'):
    obrazy = []
    pliki = sorted([f for f in os.listdir(folder) if f.endswith('.png')])
    for nazwa in pliki:
        obraz = imageio.imread(os.path.join(folder, nazwa))
        obrazy.append(obraz)
    imageio.mimsave(wyjscie, obrazy, duration=0.5)  # 0.5s na klatkę
    print(f"Utworzono animację: {wyjscie}")

# Główna funkcja symulacji
def błądzenie_losowe_na_grafie(n_wezlow=10, liczba_krokow=30, zapisz_co=1):
    G = nx.erdos_renyi_graph(n=n_wezlow, p=0.3, seed=42)

    # Upewnij się, że graf jest spójny
    while not nx.is_connected(G):
        G = nx.erdos_renyi_graph(n=n_wezlow, p=0.3)

    pozycje = nx.spring_layout(G, seed=42)
    agent = random.choice(list(G.nodes()))

    for krok in range(liczba_krokow + 1):
        if krok % zapisz_co == 0:
            rysuj_graf(G, pozycje, agent, krok)

        sąsiedzi = list(G.neighbors(agent))
        if sąsiedzi:
            agent = random.choice(sąsiedzi)

    stworz_animacje()

if __name__ == "__main__":
    błądzenie_losowe_na_grafie(n_wezlow=15, liczba_krokow=50, zapisz_co=1)
