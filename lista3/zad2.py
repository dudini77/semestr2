def converter(input, output, system):
    """
    Funkcja konwertuje końce linii w pliku tekstowym z formatu Unix na Windows lub odwrotnie.

    Args:
        input (str): Ścieżka do pliku wejściowego, który ma być przetworzony.
        output (str): Ścieżka do pliku wyjściowego, w którym zapisany zostanie wynik.
        system (str): Określa tryb konwersji. Może przyjąć dwie wartości:
                      - 'unix2windows' – zamienia końce linii z '\n' na '\r\n' (Unix → Windows),
                      - 'windows2unix' – zamienia końce linii z '\r\n' na '\n' (Windows → Unix).

    Raises:
        ValueError: Jeśli argument 'system' nie jest jedną z dozwolonych wartości ('unix2windows' lub 'windows2unix').

    Zwraca:
        None: Funkcja zapisuje wynik w pliku wyjściowym, nie zwraca żadnej wartości.

    Przykład:
        converter('plik_unix.txt', 'plik_windows.txt', 'unix2windows')
        converter('plik_windows.txt', 'plik_unix.txt', 'windows2unix')
    """
    with open(input, 'rb') as f:
        zawartosc= f.read()
    if system == 'unix2windows':
        zawartosc = zawartosc.replace(b'\r\n', b'\n')  # najpierw napraw jeśli było źle
        zawartosc = zawartosc.replace(b'\n', b'\r\n')  # zamień \n na \r\n
    elif system == 'windows2unix':
        zawartosc = zawartosc.replace(b'\r\n', b'\n')  # zamień \r\n na \n
    else:
        raise ValueError("Tryb musi być 'unix2windows' albo 'windows2unix'.")

    with open(output, 'wb') as f:
        f.write(zawartosc)

    print(f"Zamieniono i zapisano do: {output}")

plik = "unix.txt"
nowy_plik = "windows.txt"
wybor = input("podaj tryb: ")

converter(plik, nowy_plik, wybor)
