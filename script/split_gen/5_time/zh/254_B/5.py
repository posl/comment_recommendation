def problems254_b(n):
    if n == 1:
        print(1)
        return
    a = [1, 1]
    print(1)
    print(' '.join([str(i) for i in a]))
    for i in range(2, n):
        b = [1]
        for j in range(1, i):
            b.append(a[j - 1] + a[j])
        b.append(1)
        print(' '.join([str(i) for i in b]))
        a = b
