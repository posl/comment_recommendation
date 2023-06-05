def get_next_time(h, m):
    if m == 59:
        if h == 23:
            h = 0
            m = 0
        else:
            h += 1
            m = 0
    else:
        m += 1
    return h, m

if __name__ == '__main__':
    get_next_time()