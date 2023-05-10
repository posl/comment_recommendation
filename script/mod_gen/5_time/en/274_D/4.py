def is_right_angle(a, b, c):
    if (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1]) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is_right_angle()