def pow(a,b):
    if a > 0:
        return a**b
    elif a < 0:
        if b%2 == 0:
            return abs(a**b)
        else:
            return -abs(a**b)
    else:
        return 0

if __name__ == '__main__':
    pow()