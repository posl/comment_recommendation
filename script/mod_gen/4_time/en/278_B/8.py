def confusing_clock(h, m):
    if h == 23 and m > 32:
        h = 0
        m = 0
    elif m > 32:
        h += 1
        m = 0
    elif m < 32:
        m += 1
    else:
        h += 1
        m += 1
    return h, m

if __name__ == '__main__':
    confusing_clock()