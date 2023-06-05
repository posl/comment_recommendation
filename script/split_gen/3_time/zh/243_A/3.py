def problems243_a():
    v,a,b,c = map(int, input().split())
    while True:
        if v == 0:
            print('F')
            break
        v -= a
        if v == 0:
            print('F')
            break
        v -= b
        if v == 0:
            print('M')
            break
        v -= c
        if v == 0:
            print('T')
            break
