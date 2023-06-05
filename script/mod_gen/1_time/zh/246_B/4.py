def get_pos(a, b):
    if a == 0:
        return 0, 1
    elif b == 0:
        return 1, 0
    else:
        c = (a**2 + b**2)**0.5
        return a/c, b/c

if __name__ == '__main__':
    get_pos()