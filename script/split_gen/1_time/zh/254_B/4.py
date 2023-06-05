def func254_b(n):
    a = []
    for i in range(n):
        if i == 0:
            a.append([1])
        elif i == 1:
            a.append([1, 1])
        else:
            b = [1]
            for j in range(1, i):
                b.append(a[i-1][j-1] + a[i-1][j])
            b.append(1)
            a.append(b)
    return a
