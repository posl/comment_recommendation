def get_digits(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return digits[::-1]
