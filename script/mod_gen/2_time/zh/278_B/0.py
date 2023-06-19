def get_next_time(h,m):
    while True:
        m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
        if is_confuse(h,m):
            break
    return h,m

if __name__ == '__main__':
    get_next_time()