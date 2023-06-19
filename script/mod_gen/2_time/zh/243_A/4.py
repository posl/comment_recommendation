def problems243_a():
    v,a,b,c = map(int, input().split())
    while v > 0:
        v = v - a
        if v < 0:
            print('F')
            return
        v = v - b
        if v < 0:
            print('M')
            return
        v = v - c
        if v < 0:
            print('T')
            return
    return
problems243_a()
