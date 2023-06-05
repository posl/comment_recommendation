def isContain7(n):
    if n % 10 == 7:
        return True
    elif n / 10 == 0:
        return False
    else:
        return isContain7(n / 10)
