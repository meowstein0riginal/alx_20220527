from gen_sprzedaz import Transakcja

miasto = 'Katowice'
suma = 0

for rekord in Transakcja.wczytaj_plik_gen('sprzedaz.csv'):
   if rekord.miasto == miasto:
       suma += rekord.wartosc

print(suma)

