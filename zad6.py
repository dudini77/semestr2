def slupkowe_dodawanie(dzialanie):
    """
    Wyświetla działanie w formie słupka i wynik.
    
    Parametry:
    dzialanie (str): Działanie zapisane jako łańcuch znaków, np. "235+72" lub "400-123".
    
    Działanie musi być bez spacji i zawierać znak '+' lub '-' lub '*'.
    """
    if '+' in dzialanie:
        liczby = dzialanie.split('+')  # Komenda split rozdziela ciąg znaków
        znak = '+'
    elif '-' in dzialanie:
        liczby = dzialanie.split('-')
        znak = '-'
    elif '*' in dzialanie:
        liczby = dzialanie.split('*')
        znak = '*'  
    else:
        print("Nieznane działanie")
        return

    a = liczby[0]
    b = liczby[1]

    szerokosc = max(len(a), len(b)) + 2

    # Wyświetlamy słupek
    print(a.rjust(szerokosc))
    print(f"{znak} {str(b).rjust(szerokosc - 2)}")
    print('-' * szerokosc)

    if znak == '+':
        wynik = int(a) + int(b)
    elif znak == '*':
        wynik = int(a) * int(b)
    else:
        wynik = int(a) - int(b)
    print(str(wynik).rjust(szerokosc))



slupkowe_dodawanie("23*72")

