def problems243_a():
    v,a,b,c = map(int, input().split())
    while v > 0:
        if v - a < 0:
            return 'F'
        v -= a
        if v - b < 0:
            return 'M'
        v -= b
        if v - c < 0:
            return 'T'
        v -= c
print(problems243_a())
