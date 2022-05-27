# Funkcja poczatek_i_koniec jako parametr przyjmuje pewną funkcję bezargumentową.
# W wyniku zwraca zmienioną funkcję, która działa tak jak f, ale dodatkowo na początku
# i na końcu swojego działania wypisuje POCZATEK i KONIEC.
def poczatek_i_koniec(f):
   def zmieniona_funkcja():
       print('POCZATEK')
       f()
       print('KONIEC')

   return zmieniona_funkcja


def powitaj():
   print('Witamy serdecznie')

print('Normalne powitaj:')
powitaj()
print()

zmienione_powitaj = poczatek_i_koniec(powitaj)
print('Zmienione powitaj:')
zmienione_powitaj()
print()
powitaj()
