def solve():
    a, b, c, d = map(int, input().split())
    if a < b:
        print(-1)
        return
    if d == 1:
        if a <= c:
            print(0)
            return
        else:
            print(-1)
            return
    if a <= b * d:
        print(1)
        return
    if b * d < a <= c * d:
        print(2)
        return
    if c * d < a:
        print(-1)
        return
solve()
