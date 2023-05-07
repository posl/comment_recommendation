def solve(n, a):
    a.sort(reverse=True)
    ans = 0
    for i in range(n-1):
        ans += a[i] - a[i+1]
    return ans + a[-1]

if __name__ == '__main__':
    solve()