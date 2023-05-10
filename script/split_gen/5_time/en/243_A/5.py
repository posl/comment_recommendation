def problems243_a():
    v, a, b, c = map(int, input().split())
    if v >= c:
        v -= c
        if v >= b:
            v -= b
            if v >= a:
                print('T')
            else:
                print('F')
        else:
            print('M')
    else:
        print('F')
