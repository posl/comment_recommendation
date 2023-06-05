def get2(n):
    s = ""
    while n != 0:
        s = str(n % 2) + s
        n = n // 2
    return s
