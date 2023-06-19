def get_digits(n):
    digits = 0
    while n > 0:
        digits += 1
        n //= 10
    return digits
