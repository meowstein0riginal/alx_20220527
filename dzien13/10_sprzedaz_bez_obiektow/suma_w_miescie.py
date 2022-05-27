suma = 0
with open('sprzedaz.csv', mode='r', encoding='UTF-8') as plik: # mode r jest generalnie domyslne wiec nie trzeba pisac

    for linia in plik:
        t = linia.strip().split(',')

        if t[1] == 'Katowice':
            suma += float(t[5]) * float(t[6])
print(suma)
print(f'{suma:.2f}')
print('{:.2f}'.format(suma))
print('%.2f' % suma)


'''
można też to zrobić alternatywnie, ale gdyby coś się wykrzaczyło, to plik nie zostanie zamknięty

suma = 0

plik = open('sprzedaz.csv', mode='r', encoding='UTF-8') as plik: # mode r jest generalnie domyslne wiec nie trzeba pisac

plik.readline() # nie wiem co to znaczy

for linia in plik:
    t = linia.strip().split(',')
    if t[1] == 'Katowice':
        suma += float(t[5]) * float(t[6])
plik.close


print(suma)
print(f'{suma:.2f}')
print('{:.2f}'.format(suma))
print('%.2f' % suma)
'''