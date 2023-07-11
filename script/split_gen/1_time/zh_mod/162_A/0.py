def is_7_in_number(n):
    if n % 10 == 7:
        return True
    elif n < 10:
        return False
    else:
        return is_7_in_number(n // 10)
