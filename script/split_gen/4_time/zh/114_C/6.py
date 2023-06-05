def check753(n):
    if n < 357:
        return False
    if n % 2 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False
    return True
