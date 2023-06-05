def d(n):
    if n < 10:
        return n
    else:
        return d(n//10)
