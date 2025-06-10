from PIL import Image
def generator_miniatur(input, output, size):
    """
    Tworzy miniaturę obrazu i zapisuje ją do pliku.

    Args:
        input (str): Ścieżka do pliku wejściowego (oryginalnego obrazu).
        output (str): Ścieżka do pliku wyjściowego (miniatury).
        size (tuple): Maksymalne wymiary miniatury w formacie (szerokość, wysokość).

    Działanie:
        - Otwiera obraz z podanej ścieżki wejściowej.
        - Tworzy miniaturę obrazu zachowując proporcje.
        - Zapisuje miniaturę w formacie JPEG do pliku wyjściowego.
        - Wyświetla obraz.
    """
    with Image.open(input) as obraz:
        obraz.thumbnail(size)
        obraz.save(output, "JPEG")
        obraz.show()
generator_miniatur (r"C:\Users\mdude\Desktop\krowa.png", r"C:\Users\mdude\Desktop\mini_krowa.jpg", (100, 100))
