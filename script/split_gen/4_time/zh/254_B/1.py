def f(n):
    if n == 1:
        return [[1]]
    else:
        L = f(n-1)
        L1 = L[-1]
        L2 = [1]
        for i in range(1, n-1):
            L2.append(L1[i-1] + L1[i])
        L2.append(1)
        L.append(L2)
        return L
