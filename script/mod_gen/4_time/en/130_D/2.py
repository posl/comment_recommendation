def solve(n,k,a):
    ans = 0
    s = 0
    r = 0
    for l in range(n):
        while r < n and s < k:
            s += a[r]
            r += 1
        if s >= k:
            ans += n - r + 1
        s -= a[l]
    return ans

if __name__ == '__main__':
    solve()