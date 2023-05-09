def is753(n):
    if n == 0:
        return True
    if n % 10 == 7 or n % 10 == 5 or n % 10 == 3:
        return is753(n // 10)
    else:
        return False
