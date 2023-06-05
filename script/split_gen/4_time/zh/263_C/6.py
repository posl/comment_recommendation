def func(n, m):
    if n == 1:
        return [[i] for i in range(1, m+1)]
    else:
        return [i+[j] for i in func(n-1, m) for j in range(i[-1]+1, m+1)]
