def palindrom():
    x = input('Geben Sie ein Wort ein um es auf ein Palindrom zu prüfen: ')
    z = len(x) - 1
    i = 0

    while i <= z:
        res = 'Palindrom!'
        if x[i] != x[z]:
            res = 'Kein Palindrom!'
            break
        else:
            i = i + 1
            z = z - 1

    print(res)

palindrom()
