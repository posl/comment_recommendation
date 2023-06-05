def print_last_two_digits(n):
    if n < 100 or n > 999:
        return
    print(n % 100)
