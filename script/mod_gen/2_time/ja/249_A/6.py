def jog(a, b, c, d, e, f, x):
    t = 0
    aoki = 0
    takahashi = 0
    while t < x:
        for i in range(a):
            takahashi += b
            t += 1
            if t == x:
                return takahashi, aoki
        for i in range(c):
            t += 1
            if t == x:
                return takahashi, aoki
        for i in range(d):
            aoki += e
            t += 1
            if t == x:
                return takahashi, aoki
        for i in range(f):
            t += 1
            if t == x:
                return takahashi, aoki
a, b, c, d, e, f, x = map(int, input().split())
takahashi, aoki = jog(a, b, c, d, e, f, x)
