def func(n):
    l = [[1]]
    for i in range(1, n):
        l.append([1])
        for j in range(1, i):
            l[i].append(l[i-1][j-1] + l[i-1][j])
        l[i].append(1)
    return l
