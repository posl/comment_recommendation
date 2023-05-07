def nextConfusingTime(h, m):
    if h == 23 and m == 59:
        return 0, 0
    if m == 59:
        h += 1
        m = 0
    else:
        m += 1
    if h % 10 == 0 and m % 10 == 0:
        return h, m
    if h % 10 == m // 10:
        return h, m
    return nextConfusingTime(h, m)

if __name__ == '__main__':
    nextConfusingTime()