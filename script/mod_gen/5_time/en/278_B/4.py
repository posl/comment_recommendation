def confusingTime(h, m):
    while True:
        m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
        if h % 10 == m // 10 and h // 10 == m % 10:
            break
    return h, m

if __name__ == '__main__':
    confusingTime()