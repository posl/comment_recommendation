def solve(n, m, a, b, c):
    if n == 0 or m == 0:
        return 0
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    i = 0
    j = 0
    k = 0
    ans = 0
    while i < n and j < m:
        if a[i] >= c[k]:
            ans += a[i]
            i += 1
        else:
            ans += c[k]
            k += 1
            j += 1
    while i < n:
        ans += a[i]
        i += 1
    return ans

if __name__ == '__main__':
    solve()