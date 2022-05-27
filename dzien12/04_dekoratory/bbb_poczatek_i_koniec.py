def poczatek_i_koniec(f):
   def zmieniona_funkcja():
       print('POCZATEK')
       f()
       print('KONIEC')

   return zmieniona_funkcja


# Gdy mamy funkcjęwyższego rzędu, czyli taką, które bierze funkcję i w wyniku zwraca inną (zmienioną) funkcję,
# to można jej używać jako dekoratora przed definicjami zwykłych funkcji.

@poczatek_i_koniec
def powitaj():
   print('Witamy serdecznie')

@poczatek_i_koniec
def pozdrow():
   print('Na zdrowie!')

# Teraz pod oryginalnymi nazwami powitaj i pozdrow mamy zmienione funkcje.
powitaj()
print()

pozdrow()
print()

poczatek_i_koniec(powitaj)() # tutaj dopiero korzystamy ze zmienionego powitaj
print()

poczatek_i_koniec(pozdrow()) # tutaj (albo bez nawiasów przy pozdrow) wartość jest none
print()