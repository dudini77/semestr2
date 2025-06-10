import networkx as nx              # biblioteka do tworzenia i pracy z grafami
import matplotlib.pyplot as plt    # biblioteka do rysowania wykresów/grafów
import random                      


def rysuj_graf(G, pozycje, agent_pos, krok, folder='frames'):
    plt.figure(figsize=(8, 6))  # tworzy nowy wykres o podanym rozmiarze

    # Nadaje kolor "red" agentowi, reszcie węzłów "skyblue"
    kolory = ['red' if n == agent_pos else 'skyblue' for n in G.nodes()]
    
    # Rysuje graf z zaznaczeniem węzłów, pozycjami i kolorami
    nx.draw(G, pos=pozycje, with_labels=True, node_color=kolory, node_size=500)
    
    plt.title(f"Krok {krok}")  # tytuł wykresu
    plt.axis('off')            # wyłącza osie

    # Tworzy folder jeśli nie istnieje
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Zapisuje wykres jako plik PNG
    sciezka = f"{folder}/frame_{krok:03d}.png"
    plt.savefig(sciezka)
    plt.close()  # zamyka wykres 

# Funkcja tworząca animację GIF z zapisanych klatek (obrazków)
def stworz_animacje(folder='frames', wyjscie='animacja.gif'):
    obrazy = []  # lista do przechowania wszystkich obrazów
    pliki = sorted([f for f in os.listdir(folder) if f.endswith('.png')])  # sortuje pliki wg nazw
    
    # Wczytuje obrazy z plików i dodaje do listy
    for nazwa in pliki:
        obraz = imageio.imread(os.path.join(folder, nazwa))
        obrazy.append(obraz)
    
    # Tworzy plik GIF z listy obrazów
    imageio.mimsave(wyjscie, obrazy, duration=0.5)  
    print(f"Utworzono animację: {wyjscie}")

# Główna funkcja wykonująca symulację błądzenia losowego
def błądzenie_losowe_na_grafie(n_wezlow=10, liczba_krokow=30, zapisz_co=1):
    # Tworzy losowy graf z prawdopodobieństwem połączenia p = 0.3
    G = nx.erdos_renyi_graph(n=n_wezlow, p=0.3, seed=42)

    # Upewniamy się, że graf jest spójny (każdy węzeł ma połączenie)
    while not nx.is_connected(G):
        G = nx.erdos_renyi_graph(n=n_wezlow, p=0.3)

    # Oblicza pozycje węzłów do rysowania (układ sprężynowy)
    pozycje = nx.spring_layout(G, seed=42)

    # Losuje startową pozycję agenta (losowy węzeł)
    agent = random.choice(list(G.nodes()))

    # Symulacja kolejnych kroków
    for krok in range(liczba_krokow + 1):
        # Zapisuje stan grafu tylko co `zapisz_co` kroków
        if krok % zapisz_co == 0:
            rysuj_graf(G, pozycje, agent, krok)

        # Pobiera sąsiadów agenta (gdzie może pójść)
        sąsiedzi = list(G.neighbors(agent))

        # Jeśli są jacyś sąsiedzi — idzie losowo do jednego z nich
        if sąsiedzi:
            agent = random.choice(sąsiedzi)

    # Po zakończeniu błądzenia tworzy GIF ze wszystkich klatek
    stworz_animacje()

# Uruchamia program jeśli jest wykonywany jako główny plik
if __name__ == "__main__":
    
    błądzenie_losowe_na_grafie(n_wezlow=15, liczba_krokow=50, zapisz_co=1)

