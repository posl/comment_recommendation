def solve():
    n, x = map(int, input().split())
    p = 0
    for i in range(n):
        v, p = map(int, input().split())
        x -= v * p
        if x < 0:
            print(i + 1)
            return
    print(-1)
solve()
