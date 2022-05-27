
# pierwszy wariant bez zwracania wyniku sumy

def pomiar_czasu(f):
   from datetime import datetime
   def wrapper(*args, **kwargs):
       poczatek = datetime.now()
       f(*args, **kwargs)
       koniec = datetime.now()
       print('czas działania:', koniec - poczatek)

   return wrapper

@pomiar_czasu
def petla(n):
   suma = 0
   for i in range(n):
       suma += i
   return suma



petla(1000)

petla(1000_000)
