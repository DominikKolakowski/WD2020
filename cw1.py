from math import *
# zadanie 1
# Napisz pierwszy skrypt, w którym zadeklarujesz po dwie
# zmienne każdego typu, a następnie wyświetl te zmienne

def zad1_1():
    int_1 = 15
    int_2 = 9826547
    float_1, float_2 = 2.5827, -1.25821
    string_1 = 'łańcuch znaków python'
    string_2 = 'drugi łańcuch znakow'
    complex_1 = 5j + 6
    complex_2 = 1 - 2j
    print('int:', int_1, int_2)
    print('float:', float_1, float_2)
    print('string:', string_1, string_2)
    print('complex:', complex_1, complex_2)

# zadanie 2
# Stwórz skrypt kalkulator, wktórym wykorzystać
# wszystkie podstawowe działania arytmetyczne

def zad1_2():
    a=15
    b=7
    print('dodawanie:', a, '+', b, '=', a+b)
    print('odejmowanie:', a, '-', b, '=', a-b)
    print('mnożenie:', a, '*', b, '=', a*b)
    print('dzielenie:', a, '/', b, '=', a/b)
    print('dzielenie calkowite:', a, '//', b, '=', a//b)
    print('reszta z dzielenia:', a, '%', b, '=', a%b)
    print('potegowanie:', a, 'do potegi', b, '=', a**b)
    print('potegowanie:', a, 'do potegi', b, '=', pow(a,b))


# zadanie 3
# Napisz skrypt, w którym stworzysz operatory przyrostkowe dla
# operacji: +, -, *, /, **, %
def zad1_3():
    a = 4
    print('a = 4')
    a += 5
    print('a += 6:', a)
    a = 4
    a -= 6
    print('a -= 6:', a)
    a = 4
    a *= 6
    print('a *= 6:', a)
    a = 4
    a /= 6
    print('a /= 6:', a)
    a = 4
    a **= 6
    print('a **= 6:', a)
    a = 4
    a %= 6
    print('a %= 6:', a)

# zadanie 4
# Napisz skrypt, który policzy i wyświetli następujące wyrażenia:

def zad1_4():
    print('e do potegi 10 = ', pow(e, 10))
    print('(ln(5+sin^2(8)))^(1/6) = ', pow( log(5 + pow(sin(8), 2)), 1/6))
    print('⌊3,55⌋ = ', floor(3.55))
    print('⌈4,80⌉ = ', ceil(4.80))

# Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie
# wielkimi literami. Użyj odpowiedniej metody by wyświetlić
# je pisane tak, że pierwsza litera jest wielka a pozostałe małe.
# (trzeba użyć metody capitalize)
def zad1_5():
    imie = 'DOMINIK'
    nazwisko = 'KOŁAKOWSKI'
    print("Bez metody capitalize: ", imie, nazwisko)
    print("Z metodą: ",str.capitalize(imie), str.capitalize(nazwisko))

# zadanie 6
# Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu
# piosenki z powtarzającymi się słowami np. „la la la”.
# Następnie użyj odpowiedniej funkcji,
# która zliczy występowanie słowa „la”.
# (trzeba użyć metody count)
def zad1_6():
    frag = 'tra tra tra tra tra tra tra tra tra tra'
    print('"tra" powtarza sie', frag.count('tra'), 'razy')

# zadanie 7
# Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
def zad1_7():
    napis = 'dowolną zmienną łańcuchowa'
    print('napis =', napis)
    print('napis[0] =', napis[0])
    print('napis[-1] =', napis[-1])

# zadanie 8
# Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6
# i spróbuj ją podzielić na poszczególne wyrazy.(trzeba użyć metody split)
def zad1_8():
    frag = 'tra tra tra tra tra tra tra tra tra tra'
    print(str.split(frag))

# zadanie 9
# Napisz skrypt, w którym zadeklarujesz zmienne typu:
# string, float i szestnastkowe.
# Następnie wyświetl je wykorzystując odpowiednie formatowanie.
def zad1_9():
    vstring = 'tekst'
    vfloat = 243
    vhexdec = hex(255)
    print('string: %(zm)s' % {'zm': vstring})
    print('float: %(zm)f' % {'zm': vfloat})
    print('szestnastkowe: %(zm)s' % {'zm': vhexdec})

# zadanie 10
# Napisz skrypt, w którym tworzysz listę ulubionych filmów i posortuj ją.
def zad1_10():
    moje_filmy = [
        'Na skraju jutra',
        'Piraci z karaibów: Klątwa czarnej perły', 'Pulp Fiction',
        'Władca pierścieni: Dwie wieże', 'Avengers: End Game', 'Joker' ]
    print('Lista filmów przed posortowaniem:\n', moje_filmy)
    moje_filmy.sort()
    print('Lista filmów po posortowaniu:\n', moje_filmy)

# zadanie 11
# Napisz skrypt, który generuje tabelkę
# z podstawowymi wartościami funkcji trygonometrycznych.
# Wskazówka -> wykorzystaj listy i funkcje matematyczne
def zad1_11():
    tab = [
        ['kat', '0', '30', '45', '60', '90'],
        ['sin', sin(0), sin(30), sin(45), sin(60), sin(90)],
        ['cos', cos(0), cos(30), cos(45), cos(60), cos(90)],
        ['tan', tan(0), tan(30), tan(45), tan(60), tan(90)]
     ]
    print(tab[0])
    print(tab[1])
    print(tab[2])
    print(tab[3])

# zadanie 12
# Napisz skrypt, gdzie w jednej zmiennej zapiszesz
# dowolnie długie zdanie (co najmniej 5 wyrazów)
# a następnie podziel te zdanie na wyrazy tak by zostały zapisane w liście
def zad1_12():
    napis = 'To zdanie będzie miało na 100% co najmniej 5 wyrazów'
    lista_slow = str.split(napis)
    print(napis)
    print(lista_slow)


# zadanie 13
# Stwórz słownik, gdzie zapiszesz imiona i nazwiska swoich znajomych
# jako klucz proszę użyć ich przezwisk (10 elementów).
# Następnie wyświetl kilka danych odwołując się do elementów przez klucz.
def zad1_13():
    znajomi = {
        'Mati': ['Franek', 'Kowalczyk  '],
        'Sand': ['Sandra  ', 'Morawiecka'],
        'Graf': ['Franek', 'Pazura'],
        'Swg': ['Szymon', 'Włodarczyk'],
        'Kołczi': ['Adam', 'Małysz'],
        'Grzybu': ['Nicolas', 'Tesla'],
        'Mały': ['Michał', 'Kolec'],
        'Szeroki': ['Paweł', 'Drugi'],
        'Biały': ['Leonadro', 'Bielicki'],
        'Janosik': ['Janek', 'Górzysty'],
    }
    print(znajomi['Janosik'])
    print(znajomi['Grzybu'])
    print(znajomi['Sand'])

# zadanie 14
# Stwórz słownik skrótów powszechnie używanych w smsach.
# Jako klucz niech będzie skrót a jako wartość zdanie.
# Skopiuj słownik do innego słownika
def zad1_14():
    slownik_sms = {
        'LOL': 'Laughing out loud',
        'W84Me' : 'Wait for Me',
        'BTW': 'By the way',
        'IMO': 'In my opinion',
        'G8B8M8': 'great bait mate',
        'OMG': 'Oh my God',
        'THX': 'Thanks',
    }
    slownik = {
        'sms': slownik_sms,
    }
    print(slownik['sms']['W84Me'])
    print(slownik['sms']['IMO'])
    print(slownik['sms']['G8B8M8'])

# zadanie 15
# Stwórz słownik, z cyframi rzymskimi. Wybierz klucz i wartość.
def zad1_15():
    cyfry_rzymskie = {
        'I': 1, 'II': 2, 'III': 3,
        'IV': 4, 'V': 5, 'VI': 6,
        'VII': 7, 'VIII': 8, 'IX': 9,
        'X': 10, 'XI': 11, 'XII': 12,
        'XIII': 13, 'XIV': 14, 'XV ': 15,
        'XVI': 16, 'XVII': 17, 'XVIII': 18,
        'IXX': 19, 'XX': 20, 'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }
    print(cyfry_rzymskie)

# zadanie 16
# Stwórz słownik z ulubionymi grami komputerowymi.
# Pomyśl, co może być kluczem a co wartością w takim słowniku.
# Policz liczbę elementów w słowniku.
def zad1_16():
    ulubione_gry = {
        'TW3TWH': 'The Witcher 3: Wild Hunt',
        'H3': 'Heroes 3: Might and magic',
        'D2' : 'Diablo 2',
        'SC2': 'StarCraft 2',
        'LoL' : 'League of Legends',
        'PoE': 'Path of Exile',
        'Tr' : 'Trove',
        'GTA SA': 'Grand Theft Auto: San Andreas',
    }
    print('Ulubione gry :', len(ulubione_gry))


    #W miejscu X proszę podać nr zadania 
    #od 1 do 16 


NrZadania = zad1_X()

