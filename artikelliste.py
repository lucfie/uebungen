artikel = {
    111: 'Tisch',
    222: 'Stuhl',
    333: 'Lampe',
    444: 'Regal'
}
i = 0

for a in artikel:
    print('%d, %d: %s' % (i, a, artikel[a]))
    i = i + 1

