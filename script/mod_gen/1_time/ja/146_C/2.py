def d(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i

if __name__ == '__main__':
    d()