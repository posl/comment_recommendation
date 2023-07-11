def checkSeven(n):
    if n % 10 == 7:
        return True
    elif n < 10:
        return False
    else:
        return checkSeven(n // 10)
