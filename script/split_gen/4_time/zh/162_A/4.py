def isSeven(number):
    if number % 10 == 7:
        return True
    elif number / 10 == 7:
        return True
    elif number / 100 == 7:
        return True
    else:
        return False
