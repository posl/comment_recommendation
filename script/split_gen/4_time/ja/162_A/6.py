def is_contain_7(num):
    while num > 0:
        if num % 10 == 7:
            return True
        num //= 10
    return False
