def line_check(a, b, c):
    if a[0] == b[0] == c[0]:
        return True
    elif a[1] == b[1] == c[1]:
        return True
    elif (a[0] - b[0]) * (a[1] - c[1]) == (a[1] - b[1]) * (a[0] - c[0]):
        return True
    else:
        return False

if __name__ == '__main__':
    line_check()