def solve(n, m, a):
    a.sort()
    a.append(m+a[0])
    d = []
    for i in range(n):
        d.append(a[i+1]-a[i]-1)
    d.sort()
    ans = 0
    for i in range(n-1):
        ans += d[i]
    return ans

if __name__ == '__main__':
    solve()