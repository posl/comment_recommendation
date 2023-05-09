def calc(a,b):
    if a < 1 or a > 20 or b < 1 or b > 20:
        return -1
    else:
        return a * b

if __name__ == '__main__':
    calc()