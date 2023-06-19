def calc_digit(n, k):
    digit = 0
    while n > 0:
        n //= k
        digit += 1
    return digit
