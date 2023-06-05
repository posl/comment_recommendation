def snow(a,b):
    n = b - a
    x = 1
    while True:
        if n > x:
            x += 1
            n -= x
        else:
            break
    return x

if __name__ == '__main__':
    snow()