def problem258_a():
    k = int(input())
    h = 21
    m = 0
    for i in range(k):
        m += 1
        if m == 60:
            m = 0
            h += 1
    print('{:02}:{:02}'.format(h, m))
