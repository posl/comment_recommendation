def pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b > 1:
        return a * pow(a, b - 1)
    else:
        return 1 / pow(a, -b)

if __name__ == '__main__':
    pow()