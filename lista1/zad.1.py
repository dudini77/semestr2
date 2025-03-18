import random
class Vector:
    def __init__(self,elementy,wymiar=3): #metoda specjalna(__) #domyslna wartosc 3
        self.wymiar=wymiar
        self.elementy=elementy
        if self.wymiar != len(self.elementy):
            raise ValueError("Liczba elementow nie jest rowna wymiarowi wektora!")
    def losowy_wektor(self,max=10,min=-10): #cls zwraca klase
        elementy=[]
        for i in range(0,self.wymiar): #dlugosc
            elementy.append(random.randint(min,max)) #3 losowe liczby od min do max
        self.elementy=elementy
        
vector1=Vector([2,10,2,2,4],5)
vector1.losowy_wektor(100,-10)
print(vector1.elementy)






   
