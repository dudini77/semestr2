import os 
import pypdf
from pathlib import Path
def pdf_split(input, pages_num):
    """
    Dzieli plik PDF na mniejsze części zawierające określoną liczbę stron
    i zapisuje je do osobnych plików PDF w folderze 'wyjscie'.

    Args:
        input (str): Ścieżka do pliku PDF, który ma zostać podzielony.
        pages_num (int): Liczba stron w każdej części.

    Działanie:
        - Wczytuje podany plik PDF.
        - Oblicza liczbę potrzebnych plików wynikowych.
        - Dzieli dokument na fragmenty o zadanej liczbie stron.
        - Zapisuje każdy fragment jako osobny plik PDF
          o nazwie 'divide1.pdf', 'divide2.pdf', itd., w folderze 'wyjscie'.

    Przykład:
        pdf_split("plik.pdf", 5)
        # Podzieli plik "plik.pdf" na części po 5 stron każda.
    """
    reader = pypdf.PdfReader(input)
    counter= reader.get_num_pages()
    output_amount= (counter + pages_num - 1)//pages_num
    output_path = Path("wyjscie")
    output_path.mkdir(parents=True, exist_ok=True)
    for i in range (output_amount):
        writer = pypdf.PdfWriter()
        first_page= i * counter
        last_page= min(first_page+pages_num, counter)
        for page_num in range (first_page, last_page):
            writer.add_page(reader.pages[page_num])
        file_output= output_path/ f"divide{i+1}.pdf"
        with file_output.open('wb') as pdf_output:
            writer.write(pdf_output)
pdf_split("2025_04.pdf", 3)
