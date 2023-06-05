def is_confuse_time(h, m):
    if h < 10 and m < 10:
        h = str(0) + str(h)
        m = str(0) + str(m)
    elif h < 10:
        h = str(0) + str(h)
    elif m < 10:
        m = str(0) + str(m)
    else:
        pass
    if h[0] == m[1] and h[1] == m[0]:
        return True
    else:
        return False
