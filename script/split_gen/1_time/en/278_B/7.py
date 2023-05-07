def check(h,m):
    if h < 10:
        h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)
    if int(h[0]) > 2:
        return False
    if int(h[0]) == 2 and int(h[1]) > 3:
        return False
    if int(m[0]) > 5:
        return False
    return True
