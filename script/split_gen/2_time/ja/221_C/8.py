def get_max_multiplied_digit(n):
    max_multiplied_digit = 0
    for i in range(1, len(n)):
        a = int(n[:i])
        b = int(n[i:])
        max_multiplied_digit = max(max_multiplied_digit, a * b)
    return max_multiplied_digit
