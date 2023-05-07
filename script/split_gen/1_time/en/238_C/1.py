def get_digit(n):
    digit = 0
    while n > 0:
        n //= 10
        digit += 1
    return digit
