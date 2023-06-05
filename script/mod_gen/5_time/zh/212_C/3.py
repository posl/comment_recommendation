def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 10**9
    i = 0
    for x in b:
        while i < n and a[i] <= x:
            i += 1
        if i > 0:
            ans = min(ans, abs(x-a[i-1]))
        if i < n:
            ans = min(ans, abs(a[i]-x))
    print(ans)
solve()
