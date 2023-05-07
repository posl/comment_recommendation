def next_confusing_time(h, m):
    if h == 23 and m == 59:
        return 0, 0
    if m == 59:
        return h + 1, 0
    if (m // 10) % 10 == m % 10:
        return h, m + 1
    if m % 10 == 0:
        return h, m + 1
    if (m // 10) % 10 == 0:
        return h, m + 10
    return h, m + 10 - (m % 10)

if __name__ == '__main__':
    next_confusing_time()