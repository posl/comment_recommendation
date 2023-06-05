def check_apple_tree(n, d):
    if n % (d * 2 + 1) == 0:
        return n // (d * 2 + 1)
    else:
        return n // (d * 2 + 1) + 1

if __name__ == '__main__':
    check_apple_tree()