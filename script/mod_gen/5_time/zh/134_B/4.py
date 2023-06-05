def check_apple_tree(N, D):
    if N % (2*D + 1) == 0:
        return N // (2*D + 1)
    else:
        return N // (2*D + 1) + 1

if __name__ == '__main__':
    check_apple_tree()