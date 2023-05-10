def check(n):
    if n % 2 == 0:
        if n % 3 == 0 or n % 5 == 0:
            return True
        else:
            return False
    else:
        return True
