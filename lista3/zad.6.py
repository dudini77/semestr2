import requests
from bs4 import BeautifulSoup
import webbrowser
def article_dowloader():
    """
    Losuje przypadkowy artykuł z Wikipedii i pobiera jego tytuł oraz adres URL.

    Zwraca:
    tuple: (tytuł artykułu jako str, URL artykułu jako str)
    """
    url = "https://en.wikipedia.org/wiki/Special:Random"
    answer = requests.get(url)
    url2 = answer.url
    soup = BeautifulSoup(answer.text, "html.parser")  
    title = soup.find('h1', id="firstHeading")  
    title2 = title.text if title else "Nieznany tytuł"
    return title2, url2  
def question(title):
    """
    Pyta użytkownika, czy chce otworzyć dany artykuł.

    Argumenty:
    title (str): Tytuł artykułu do wyświetlenia.

    Zwraca:
    bool: True jeśli użytkownik chce otworzyć artykuł, False w przeciwnym przypadku.
    """
    print(f"Tytuł artykułu: {title}")
    choice= input("Czy chcesz go otworzyć? Tak lub nie: ").strip().lower() 
    return choice == "tak"
def browser(url):
    """
    Otwiera podany URL w domyślnej przeglądarce internetowej.

    Argumenty:
    url (str): Adres URL do otwarcia.

    Zwraca:
    None
    """
    webbrowser.open(url)
def main():
    """
    Główna funkcja programu:
    - losuje artykuł z Wikipedii,
    - wyświetla tytuł,
    - pyta użytkownika o chęć otwarcia,
    - otwiera artykuł w przeglądarce jeśli użytkownik się zgodzi.

    Zwraca:
    None
    """
    title, url= article_dowloader()
    if question(title):
        browser(url)
main()