def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] >= 0:
            ans += a[i]
            a[i] = 0
    a.sort()
    a.reverse()
    for i in range(m):
        if a[i] < 0:
            ans -= a[i]
    print(ans)

if __name__ == '__main__':
    solve()