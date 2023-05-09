def get100s(d, n):
    if d == 0:
        return n
    elif d == 1:
        return n * 100
    else:
        return n * 10000

if __name__ == '__main__':
    get100s()