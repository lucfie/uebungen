def einlesen():
    n = 1
    liste = list()
    while n != 0:
        try:
            n = int(input('Natürliche Zahl eingeben [beenden mit 0]:'))
            if int(n) > 0:
                liste.append(int(n))
        except ValueError:
            print('Ungültige Eingabe!')

    print(liste)


einlesen()

