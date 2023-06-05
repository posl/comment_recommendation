def problems241_a():
    a = raw_input()
    a = a.split()
    a = map(int, a)
    k = 0
    for i in range(3):
        k = a[k]
    print k
