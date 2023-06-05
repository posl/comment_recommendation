def solve(n, a):
    ans = 0
    for l in range(n):
        for r in range(l, n):
            x = a[l]
            for i in range(l, r+1):
                x = min(x, a[i])
            ans = max(ans, x*(r-l+1))
    return ans

if __name__ == '__main__':
    solve()