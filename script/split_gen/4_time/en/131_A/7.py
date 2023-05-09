def check_number(number):
    if number[0] == number[1]:
        return False
    elif number[1] == number[2]:
        return False
    elif number[2] == number[3]:
        return False
    else:
        return True
