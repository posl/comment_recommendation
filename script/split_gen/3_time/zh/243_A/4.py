def solve():
    v,a,b,c = map(int, input().split())
    while True:
        if v < a:
            return 'F'
        v -= a
        if v < b:
            return 'M'
        v -= b
        if v < c:
            return 'T'
        v -= c
print(solve())
