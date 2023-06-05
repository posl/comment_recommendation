def solve():
    a, b, c, d = map(int, input().split())
    if a < b * d:
        print(-1)
        return
    print((a - 1) // (b * d - c) + 1)
solve()
