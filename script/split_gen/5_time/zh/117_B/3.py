def check(n, l):
    l.sort()
    if l[n-1] < sum(l[:n-1]):
        return True
    return False
