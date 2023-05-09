def check753(num):
    if num >= 1000:
        if num % 10 == 7:
            return check753(num // 10)
        elif num % 10 == 5:
            return check753(num // 10)
        elif num % 10 == 3:
            return check753(num // 10)
        else:
            return False
    else:
        if num == 7:
            return True
        elif num == 5:
            return True
        elif num == 3:
            return True
        else:
            return False
