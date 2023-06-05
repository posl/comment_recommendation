def problems243_a():
    v, a, b, c = map(int, input().split())
    sum = 0
    while True:
        sum += 1
        if v < a:
            print('F')
            break
        v -= a
        if v < b:
            print('M')
            break
        v -= b
        if v < c:
            print('T')
            break
        v -= c
problems243_a()
