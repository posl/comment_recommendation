def solve(n, a):
    from collections import Counter
    c = Counter(a)
    ans = 0
    for k in range(1, n+1):
        ans += c[k] * (c[k] - 1) // 2
    for k in range(1, n+1):
        print(ans - (c[a[k-1]] - 1))

if __name__ == '__main__':
    solve()