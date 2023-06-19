def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans += a[i] * a[i]
        ans -= 2 * a[i] * sum(a[:i])
        ans += sum(a[:i]) * sum(a[:i])
    print(ans)
solve()
