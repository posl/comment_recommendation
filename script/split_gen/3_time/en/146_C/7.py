def num_digits(n):
    if n == 0:
        return 1
    return int(math.log10(n)) + 1
