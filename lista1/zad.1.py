import random
class Vector:
    def __init__(self,elementy,wymiar=3): #metoda specjalna(__) #domyslna wartosc 3
        self.wymiar=wymiar
        self.elementy=elementy
        if self.wymiar != len(self.elementy):
            raise ValueError("Liczba elementow nie jest rowna wymiarowi wektora!")
    def losowy_wektor(self,max=10,min=-10): 
        elementy=[]
        for i in range(0,self.wymiar): #dlugosc
            elementy.append(random.randint(min,max)) #3 losowe liczby od min do max
        self.elementy=elementy
    def __add__(self,other):    
        if self.wymiar != other.wymiar:
            raise ValueError("Wektory muszą być tych samych wymiarów")
        return Vector([a + b for a, b in zip(self.elementy, other.elementy)]) 
    def __sub__(self,other):
        if self.wymiar != other.wymiar:
            raise ValueError("Wektory muszą być tych samych wymiarów")
        return Vector([a - b for a, b in zip(self.elementy, other.elementy)])
    def __mul__(self,skalar):
        return Vector([skalar*a for a in self.elementy])
    def __rmul__(self,skalar):
        return Vector([a*skalar for a in self.elementy])
    def iloczyn_skalarny(self,other):
        if self.wymiar != other.wymiar:
            raise ValueError("Wektory muszą być tych samych wymiarów")
        return sum([a * b for a, b in zip(self.elementy, other.elementy)])
    def __str__(self):
        return f"Jest to wektor o współrzędnych({', '.join(map(str,self.elementy))})"
    def suma_elementów(self):
        return sum (self.elementy)
    def vector_dlugosc(self):
        return sum(x**2 for x in self.elementy)**(0.5)
    def __getitem__(self,indeks):
        return self.elementy[indeks]
    def __contains__(self,item):
        return item in self.elementy 


        
vector1=Vector([2,10,2,5],3)
#print(5*vector1)
#vector1.losowy_wektor(100,-10)
#print(vector1.elementy)
vector2=Vector([1,2,3])
#vector4=Vector([3,2,1])
#print(vector2)
#v3 = vector4 * vector2
#print(vector1)
print(vector1.iloczyn_skalarny(vector2))
#print(v3.elementy)
#print(vector2.suma_elementów())
#print(vector1.vector_dlugosc())
#print(vector1[2])
#print(10 in vector1)
print(vector1)




   
