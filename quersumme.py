def quersumme(zahl):
    s = str(zahl)
    q = 0
    for n in s:
        q = q + int(n)
    print('Quersumme von %d = %d' % (zahl, q))

quersumme(123)