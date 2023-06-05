def is753(num):
    if num < 357:
        return False
    if num % 2 == 0:
        return False
    if num % 5 == 0:
        return False
    if num % 7 == 0:
        return False
    if num % 3 != 0:
        return False
    return True
