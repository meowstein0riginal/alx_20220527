# wypisujemy linie wraz z numerem
with open('sprzedaz.csv', mode='r', encoding='UTF-8') as plik: # mode r jest generalnie domyslne wiec nie trzeba pisac
    for nr, linia in enumerate(plik, 2): # 2 to wartość początkowa
        print(f'{nr:6}: {linia}', end='') # 6 to wcięcie, jak zrobimy tylko ^ to środkuje, jak < albo > to wyrównuje do lewejprawej, jak damy np. 06 to wcięcie zastąpi zerami