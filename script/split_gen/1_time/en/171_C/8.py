def getDogName(n):
    n -= 1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    name = ""
    while n > 25:
        name += alphabet[n % 26]
        n = n // 26 - 1
    name += alphabet[n % 26]
    return name[::-1]
