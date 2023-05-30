def solve():
    n, x = map(int, input().split())
    a_b = [tuple(map(int, input().split())) for _ in range(n)]
    a_b.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for a, b in a_b:
        ans += a + b
        if ans > x:
            print(ans - a - b)
            return
    print(ans)
solve()
