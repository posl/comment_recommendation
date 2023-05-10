def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    l = 0
    for r in range(n):
        s += a[r]
        while s >= k:
            ans += n - r
            s -= a[l]
            l += 1
    print(ans)

if __name__ == '__main__':
    solve()