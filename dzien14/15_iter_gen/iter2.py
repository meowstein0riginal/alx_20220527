class IteratorParzystych:
   def __init__(self, start, stop):
       self.current = start
       self.stop = stop

   def __next__(self):
       if self.current > self.stop:
           raise StopIteration
       try:
           return self.current
       finally:
           self.current += 2


class Parzyste:
   def __init__(self, limit):
       self.limit = limit

   def __iter__(self):
       return IteratorParzystych(0, self.limit)


obiekt = Parzyste(100)
for x in obiekt:
   print(x)


