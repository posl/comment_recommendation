def century(n):
    if n % 100 == 0:
        return int(n/100)
    else:
        return int(n/100) + 1
