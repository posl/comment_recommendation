def get_next_time(h, m):
    if m < 59:
        m += 1
    else:
        m = 0
        if h < 23:
            h += 1
        else:
            h = 0
    return h, m
