def century(N):
    if N % 100 == 0:
        return N // 100
    else:
        return N // 100 + 1
