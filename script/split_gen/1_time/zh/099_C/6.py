def withdraw(N):
    if N == 0:
        return 0
    elif N < 6:
        return N
    else:
        n = 1
        while 6**n <= N:
            n += 1
        n -= 1
        return 1 + withdraw(N - 6**n)
