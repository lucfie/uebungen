def zaehle_kons(str):
    i = 0
    v = ['a', 'e', 'i', 'o', 'u']
    for ch in str:
        if ch not in v:
            i = i + 1
    return i


print(zaehle_kons('abcdefg'))

