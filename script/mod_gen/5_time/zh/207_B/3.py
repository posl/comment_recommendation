def count(n, b, c, d):
    if n > c*d:
        return -1
    else:
        if n % d == 0:
            return 0
        else:
            return d - n % d

if __name__ == '__main__':
    count()