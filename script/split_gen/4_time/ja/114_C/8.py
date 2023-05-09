def is753(n):
    if n < 357:
        return False
    if n % 10 == 7 or n % 10 == 5 or n % 10 == 3:
        if n // 10 == 0:
            return True
        else:
            return is753(n // 10)
    else:
        return False
