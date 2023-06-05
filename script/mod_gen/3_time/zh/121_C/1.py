def solve():
    n, m = map(int, input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort()
    ans = 0
    for a, b in ab:
        if m > b:
            ans += a * b
            m -= b
        else:
            ans += a * m
            break
    print(ans)
solve()
