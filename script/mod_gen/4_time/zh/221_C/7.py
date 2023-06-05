def split(n):
    l = []
    while n:
        l.append(n%10)
        n //= 10
    l.reverse()
    return l

if __name__ == '__main__':
    split()