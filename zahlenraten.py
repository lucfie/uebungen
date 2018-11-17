import random

x = random.randint(1, 100)
i = 0
y = 0

while y != x:
    i = i + 1
    try:
        y = int(input('Gesucht wird eine ganze Zahl zwischen 1...100. Raten sie! Ihre Zahl bitte:'))
        if y > x:
            print('Die Zahl %d war leider größer als die gesuchte Zahl. Versuchen Sie es noch einmal.' % y)
        else:
            print('Die Zahl %d war leider kleiner als die gesuchte Zahl. Versuchen Sie es noch einmal.' % y)
    except ValueError:
        print('Ungültige Eingabe!')

print('Gewonnen! Sie haben nur %d Versuche gebraucht!' % i)



