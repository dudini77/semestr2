def bracket(sentence):
    """
    Sprawdza poprawność nawiasów w zadanym ciągu znaków.

    Argumenty:
    sentence (str): Ciąg znaków zawierający nawiasy i inne znaki.

    Zwraca:
    bool: True jeśli nawiasy są poprawnie sparowane i zagnieżdżone, False w przeciwnym przypadku.
    """
    stos = []
    brackets = {')': '(', ']': '[', '}': '{'}
    for i in sentence: 
        if i in brackets.values():
            stos.append(i)
        elif i in brackets.keys():
            if not stos or stos[-1] != brackets[i]:
                return False 
            stos.pop
    return len(stos) == 0
sentence = input()
a=bool 
a= bracket(sentence)
if a == True:
    print("Good") 
else:
    print("Not good")
