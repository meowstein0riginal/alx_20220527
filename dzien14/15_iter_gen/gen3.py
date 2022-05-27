# Skończony generator liczb parzystych

def parzyste(limit):
    liczba = 0
    while limit >= liczba:
        yield liczba
        liczba += 2


for x in parzyste(1000):
   print(x)

