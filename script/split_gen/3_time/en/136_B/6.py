def count_odd_digits(n):
    if n > 9:
        return 10 ** (len(str(n)) - 1) // 2 + count_odd_digits(n % (10 ** (len(str(n)) - 1)))
    else:
        return 1
