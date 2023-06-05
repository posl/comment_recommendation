def get_digits(num):
    digits = 0
    while num:
        num //= 10
        digits += 1
    return digits
