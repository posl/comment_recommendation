def isContainSeven(num):
    if num % 10 == 7:
        return True
    elif num // 10 % 10 == 7:
        return True
    elif num // 100 % 10 == 7:
        return True
    else:
        return False
