import qrcode
import cv2
def qr_generator(data, output):
    qr = qrcode.make(data)
    qr.save(output)
    print("Utworzono kod QR")
    """
    Tworzy kod QR na podstawie podanych danych i zapisuje go do pliku.

    Argumenty:
    data (str): Dane do zakodowania w QR (np. tekst, link).
    output (str): Ścieżka do pliku wyjściowego, w którym zostanie zapisany kod QR (np. 'qr.png').

    Zwraca:
    None
    """
def qr_reader(input):
    """
    Odczytuje dane z obrazu kodu QR.

    Argumenty:
    input (str): Ścieżka do pliku obrazu zawierającego kod QR.

    Zwraca:
    None
    (drukuje odczytane dane w konsoli lub informację o braku kodu QR)
    """
    qr = cv2.imread(input)
    detector = cv2.QRCodeDetector()
    data, frame, _ = detector.detectAndDecode(qr)
    if data:
        print("Odczytano kod")
        print(data)
    else:
        print("To nie jest kod qr")
qr_generator("https://www.youtube.com/watch?v=0I5FFrdajfY", "qr.png")
qr_reader("krowa.png")