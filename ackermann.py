def ack(n, m):
    while n != 0:
        if m == 0:
            m = 1
        else:
            m = ack(n, m - 1)
        n = n - 1
    return m + 1


print(ack(3, 4))
