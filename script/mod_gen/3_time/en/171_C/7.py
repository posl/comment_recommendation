def getDogName(n):
    base = 26
    name = ''
    while n > 0:
        n -= 1
        name = chr(ord('a') + n % base) + name
        n //= base
    return name

if __name__ == '__main__':
    getDogName()