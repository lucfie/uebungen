arr = [45, 2, 50, 3, 75, 8, 100, 342, 23423, 4]
min = arr[0]
max = arr[0]

for e in arr:
    if min > e:
        min = e
    if max < e:
        max = e

print(min, max)


