def func(n, m):
    if n == 1:
        for i in range(1, m+1):
            print(i)
    else:
        for i in range(1, m+1):
            func(n-1, i)
