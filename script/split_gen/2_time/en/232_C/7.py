def check(a,b,c,d):
    for i in range(len(a)):
        if a[i] == c[i]:
            continue
        else:
            return False
    for i in range(len(b)):
        if b[i] == d[i]:
            continue
        else:
            return False
    return True
