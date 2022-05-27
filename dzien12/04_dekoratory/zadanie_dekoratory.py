'''
Zaimplementuj zestaw dekoratorów otaczających zwracany przez
funkcję napis tagami HTML (pogrubienie, podkreślenie,
przekreślenie):
Przykład użycia:

@bold
@italic
def foo(arg):
return f'To jest {arg}'
'''

def bold(f):
    def wrapper(*args, **kwargs):
        wynik = f'<b>{f(*args, **kwargs)}</b>'
        return wynik
    return wrapper

@bold
def tekst(input):
    return input

print(tekst('THIS IS BOLD'))

###############

def italic(f):
    return lambda arg: f'<i>{f(arg)}</i>'

@italic
def tekst_2(arg):
    return arg

print(tekst_2('THIS IS ITALIC'))

### lub

def italic2(f):
    def wrapper(input2):
        return f'<i>{f(input2)}</i>'
    return wrapper

@italic2
def tekst_3(input2):
    return input2

print(tekst_3('THIS IS ITALIC'))



'''
# rozwiązanie trenera

def bold(f):
   def wrapper(arg):
       napis = f(arg)
       return f'<b>{napis}</b>'
   return wrapper

# Zmodyfikowana wersja funkcji, którą zwraca dekorator, może być zdefiniowana
# nie tylko konstrukcją def
def italic(f):
   return lambda arg: f'<i>{f(arg)}</i>'

@bold
@italic
def foo(arg):
   return f'To jest {arg}'


foo('Ala')
print(foo('Ola'))

'''