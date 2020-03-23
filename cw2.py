import math 
import sys


def zad2_1():
    print("Proszę podać dowolne zdanie: ")
    zdanie = sys.stdin.readline()
    print('W tym zdaniu jest :', zdanie.count(' ') ,'spacji')



def zad2_2():
    print('podaj pierwszą liczbe:')
    liczba1 = sys.stdin.readline()
    print('podaj drugą liczbe:')
    liczba2 = sys.stdin.readline()
    sys.stdout.write('wynik: ' + str(float(liczba1) * float(liczba2)))



def zad2_3():
    print('Lista operatorów w instrukcjach warunkowych')
    print('Równe: a == b')
    print('Różne: a != b')
    print('Mniejsze: a < b')
    print('Mniejsze bądź równe: a <= b')
    print('Większe: a > b')
    print('Większe bądź równe: a >= b')



def zad2_4():
    liczba = int(input('podaj liczbe calkowitą: '))
    if liczba >= 0:
        print('|', liczba, '| = ', liczba, end='')
    else:
        print('|', liczba, '| = ', liczba * (-1), end='')



def zad2_5():
    a = int(input('Podaj  a: '))
    b = int(input('Podaj  b: '))
    c = int(input('Podaj  c: '))
    if a > 0 and a <= 10:
        print(' a należy do (0,10>')
    else:
        print(' a nie należy do (0,10>')
    if a > b or b > c:
        print(' a > b lub b > c ')
    else:
        print(' a < b lub b < c ')



def zad2_6():
    print('Liczby podzielne przez 5 do 200>: ')
    for licznik in range(0, 201, 5):
        print(str(licznik), end=' ')



def zad2_7():
    lista = []
    for pentla in range(1, 5, 1):
        liczba = input('podaj '+' liczbe: ')
        lista.append(int(liczba))
    for pentla in range(0, 4, 1):
        print(str(lista[pentla]) + '^2 = ' + str(lista[pentla] ** 2))



def zad2_8():
    lista = []
    i = 0
    while i < 4:
        liczba = input('Podaj liczbę: ')
        lista.append(int(liczba))
        i += 1
    print(lista)



def zad2_9():
    liczba = int(input('Podaj liczbę wielocyfrową: '))
    suma = 0
    while (liczba != 0):
        suma = suma + liczba % 10
        liczba = liczba // 10
    print('Suma cyfr = ' + str(suma))



def zad2_10():
    x = int(input('podaj wielkość wieży, ale nie więcej niż 10: ''\n'))
    if x >10:
        print('nie więcej niż 10')
        return 0;
    for i in range(0, x, 1):
        for j in range(0, i + 1, 1):
            print('A', end='')
        print()



def zad2_11():
    h = 0
    while (h < 3 or h > 9):
        print('Wysokość ma być mniędzy <3,9>')
        h = int(input('Podaj wysokość: '))
    h_parzysta = False
    if (h % 2 == 0):
        h_parzysta = True
        h = h - 1
    s = h // 2
    kolo = 1
    for i in range(0, h // 2, 1):
        for j in range(0, s, 1):
            print(' ', end='')
        s = s - 1
        for j in range(0, kolo, 1):
            print('O', end='')
        kolo = kolo + 2
        print()


    for i in range(0, h, 1):
        print('O', end='')
    print()
    if (h_parzysta == True):
        for i in range(0, h, 1):
            print('O', end='')
        print()


    s = 1
    kolo = h - 2
    for i in range(0, h // 2, 1):
        for j in range(0, s, 1):
            print(' ', end='')
        s = s + 1
        for j in range(kolo, 0, -1):
            print('O', end='')
        kolo = kolo - 2
        print()


def zad2_12():

    for i in range(1, 11, 1):
        if (len(str(i)) == 1):
            print('|  ' + str(i) + '  |', end='')
        else:
            print('|  ' + str(i) + ' |', end='')
        for j in range(1, 11, 1):
            liczba = int(i) * int(j)


            if len(str(liczba)) == 1:
                print('  ' + str(liczba) + '  |', end='')
            elif len(str(liczba)) == 2:
                print('  ' + str(liczba) + ' |', end='')
            else:
                print(' ' + str(liczba) + ' |', end='')
        print('')


def zad2_14():
    liczba = float(input('podaj liczbę rzeczywistą >0: '))
    try:
        wynik = math.sqrt(liczba)
        for i in range(0, len(str(liczba)), 1):
            print(end='')
        print()
        print('Pierwsiastek z liczby: ',str(liczba) + ' = ' + str(wynik))
    except ValueError:
        print('Nie można obliczyć pierwiastka z liczby <0 ')


def zad2_15():
    try:
        liczba = float(input('podaj liczbę: '))
        print('Podałeś liczbę: ',liczba)
    except:
        print('Nie wprowadziałeś liczby')

   #W miejscu X wstaw nr zadania do wywołania
   # od 1 do 15 BEZ 13 

NrZadania = zad2_15()
