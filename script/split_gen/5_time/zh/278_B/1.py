def isConfuseTime(h, m):
    if h == 0:
        h = 24
    h1 = int(str(m)[::-1])
    m1 = int(str(h)[::-1])
    if h1 <= 23 and m1 <= 59:
        return True
    else:
        return False
