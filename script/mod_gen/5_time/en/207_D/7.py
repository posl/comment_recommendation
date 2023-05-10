def check(a,b,c,d):
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    if a == c and b == d:
        return True
    else:
        return False

if __name__ == '__main__':
    check()