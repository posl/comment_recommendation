def check_apple_tree(N, D):
    check = 0
    if N % (2 * D + 1) == 0:
        check = N // (2 * D + 1)
    else:
        check = N // (2 * D + 1) + 1
    return check
