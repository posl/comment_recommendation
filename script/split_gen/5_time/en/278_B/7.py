def confusing_time(h, m):
    while True:
        if m == 59:
            h += 1
            m = 0
        else:
            m += 1
        if h == 24:
            h = 0
        if int(str(m)[::-1]) == h:
            return h, m
h, m = map(int, input().split())
h, m = confusing_time(h, m)
print("{0:02d} {1:02d}".format(h, m))
