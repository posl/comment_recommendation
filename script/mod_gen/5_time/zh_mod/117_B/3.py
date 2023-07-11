def check(n, l):
    l.sort()
    if l[n-1] < sum(l[:n-1]):
        return True
    return False

if __name__ == '__main__':
    check()