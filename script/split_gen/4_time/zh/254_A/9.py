def get_last_two_digits(num):
    if num < 100 or num > 999:
        return None
    return num % 100
