def check_apple_tree(N, D):
    if N % (2*D + 1) == 0:
        return N // (2*D + 1)
    else:
        return N // (2*D + 1) + 1
