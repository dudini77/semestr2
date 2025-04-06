import random

def generuj_haslo():
    """
    Generuje losowe hasło składające się z 8 znaków ASCII.
    
    Hasło zawiera znaki o kodach od 32 do 126 (czyli wszystkie drukowalne znaki ASCII,
    w tym litery, cyfry, znaki specjalne i spacje).

    Returns:
        str: Wygenerowane hasło.
    """
    haslo = ''
    for i in range(0, 8):
        haslo += chr(random.randint(32, 126))
    return haslo

# Przykład użycia
print("Hasło to:", generuj_haslo())