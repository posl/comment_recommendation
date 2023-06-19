def get_time(k):
    h = 21
    m = 0
    for i in range(k):
        m += 1
        if m == 60:
            m -= 60
            h += 1
            if h == 24:
                h -= 24
    return h, m

if __name__ == '__main__':
    get_time()