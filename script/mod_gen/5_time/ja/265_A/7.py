def calc(x,y,n):
    if n%3 == 0:
        return n/3 * y
    else:
        return (n/3 * y) + (n%3 * x)

if __name__ == '__main__':
    calc()