def g1(n):
    s = str(n)
    l = list(s)
    l.sort(reverse = True)
    s = ''.join(l)
    return int(s)

if __name__ == '__main__':
    g1()