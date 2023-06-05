def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a)
    b = sorted(b)
    ans = 0
    for i in range(n):
        if k < a[i]:
            break
        k -= a[i]
        ans += 1
    for i in range(m):
        if k < b[i]:
            break
        k -= b[i]
        ans += 1
    print(ans)
