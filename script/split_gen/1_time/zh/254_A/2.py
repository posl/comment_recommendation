def last_two_digits(n):
    if n < 100 or n > 999:
        return None
    return n % 100
