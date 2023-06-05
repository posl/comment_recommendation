def check_apple_tree(n, d):
    if n % (2 * d + 1) == 0:
        return n // (2 * d + 1)
    else:
        return n // (2 * d + 1) + 1
