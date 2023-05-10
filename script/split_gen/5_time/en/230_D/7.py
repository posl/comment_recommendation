def solve():
    n, d = map(int, input().split())
    a = [0] * n
    for i in range(n):
        l, r = map(int, input().split())
        a[i] = (l, r)
    a.sort()
    ans = 0
    for i in range(n):
        l, r = a[i]
        while l <= r:
            ans += 1
            l += d
    print(ans)
solve()
