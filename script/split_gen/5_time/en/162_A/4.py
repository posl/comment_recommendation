def check_seven(number):
    if number % 10 == 7 or (number // 10) % 10 == 7 or number // 100 == 7:
        return True
    else:
        return False
