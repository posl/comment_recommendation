def jump(n, x, ab):
    pos = 0
    for i in range(n):
        pos += ab[i][0]
        if pos > x:
            return False
        pos += ab[i][1]
    if pos > x:
        return False
    else:
        return True
