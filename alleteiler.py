def alleTeiler(z):
    at = []
    i = 1
    while i < z:
        if z % i == 0:
            at.append(i)
        i = i + 1
    return at


print(alleTeiler(12))

print(sum(alleTeiler(28)))


def ideal(z):
    return sum(alleTeiler(z)) == z


print(ideal(28))


def prim(z):
    return len(alleTeiler(z)) == 1


print(prim(28))