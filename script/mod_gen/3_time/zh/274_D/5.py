def is_right_angle(a,b,c):
    a1 = (b[0] - a[0]) * (c[0] - b[0]) + (b[1] - a[1]) * (c[1] - b[1])
    a2 = (b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1])
    a3 = (c[0] - b[0]) * (c[0] - b[0]) + (c[1] - b[1]) * (c[1] - b[1])
    if a1 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is_right_angle()