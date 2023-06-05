def check_seven(num):
    while num > 0:
        if num % 10 == 7:
            return True
        num = num // 10
    return False
