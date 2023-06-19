def problem273_b(x, k):
    y = x
    for i in range(k):
        y = round(y, -i)
    print(int(y))
problem273_b(2048, 2)
problem273_b(1, 15)
problem273_b(999, 3)
problem273_b(314159265358979, 12)
