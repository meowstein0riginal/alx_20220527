'''
Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora
swobodnego na dwuwymiarowej płaszczyźnie. Wektory powinny
mieć możliwość dodawania, odejmowania, mnożenia (przez liczbę),
porównywania (po długości) oraz powinny posiadać czytelną
reprezentację napisową.


Przykład użycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=3, y=2)
vector_3 = vector_1 + vector_2

import math

class Vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

#    def dlugosc(self):



    def __str__(self):
        return f'X={self.x}, Y={self.y}, ILOCZYN={ddd}'

vector_1 = Vector(1, 2)
vector_2 = Vector(3, 2)
vector_3 = vector_1 + vector_2
print(vector_3)

################
'''
class Vector:
   def __init__(self, x=0, y=0):
       self.x = x
       self.y = y

   def __str__(self):
       return f'<{self.x},{self.y}>'

   def __repr__(self):
       return f'Vector({self.x},{self.y})'

   def __add__(self, other):
       return Vector(self.x + other.x, self.y + other.y)

   def __sub__(self, other):
       return Vector(x=self.x - other.x, y=self.y - other.y)

   def __mul__(self, num):
       return Vector(self.x * num, self.y * num)

   def __rmul__(self, num):
       return Vector(self.x * num, self.y * num)

   # dekorator @property powoduje, że aby odczytać wynik tej metody, nie używa się już wywołania
   # v.dlugosc()
   # tylko stosuje się zapis taki jak przy odczycie atrybutu (zmiennej)
   # v.dlugosc
   @property
   def dlugosc(self):
       return (self.x ** 2 + self.y ** 2) ** 0.5

   def __eq__(self, other):
       return self.dlugosc == other.dlugosc

   def __lt__(self, other):
       return self.dlugosc < other.dlugosc

   def __le__(self, other):
       return self.dlugosc <= other.dlugosc

   def __bool__(self):
       return self.dlugosc != 0.0


def proste_testy():
   a = Vector(3, 4)
   b = Vector(5, 11)
   print('a:', a)
   print('b:', b)

   print('repr a:', repr(a))
   print('repr b:', repr(b))
   print()

   wynik = a + b
   print(wynik)

   wynik = a - b
   print(wynik)

   wynik = a * 5
   print(wynik)

   wynik = 3 * a
   print(wynik)

   print(a.dlugosc)
   print(a > b)
   print(a <= b)

   if a:
       print('Wektor a nie jest zerowy')



proste_testy()
