def pow(a, b):
    if b == 0:
        return 1
    else:
        return a * pow(a, b - 1)

if __name__ == '__main__':
    pow()