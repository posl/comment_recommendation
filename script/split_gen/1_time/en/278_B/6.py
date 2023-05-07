def next_confusing_time(h, m):
    if h == 23 and m == 59:
        return 0, 0
    if m == 59:
        return h+1, 0
    if m >= 30:
        return h, 30
    if m >= 20:
        return h, 20
    if m >= 10:
        return h, 10
    if m >= 0:
        return h, 0
