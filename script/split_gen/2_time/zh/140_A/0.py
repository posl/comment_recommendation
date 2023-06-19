def get_passwords(n):
    if n == 1:
        return 1
    elif n == 2:
        return 8
    else:
        return 9 * 8 ** (n - 1)
