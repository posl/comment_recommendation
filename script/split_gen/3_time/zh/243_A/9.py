def problems243_a():
    v, a, b, c = map(int, input().split())
    while v > 0:
        if v >= a:
            v -= a
        else:
            print("F")
            break
        if v >= b:
            v -= b
        else:
            print("M")
            break
        if v >= c:
            v -= c
        else:
            print("T")
            break
