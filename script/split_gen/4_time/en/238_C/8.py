def f(n):
    if n<=9:
        return n
    else:
        k = len(str(n))
        return 9*(k-1)+sum([int(str(n)[i]) for i in range(k)])-1
