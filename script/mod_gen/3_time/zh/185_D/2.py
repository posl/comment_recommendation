def solve(n, m, a):
    a.sort()
    a.append(n+1)
    k = 0
    for i in range(m+1):
        d = a[i+1] - a[i] - 1
        if d > 0:
            k = max(k, d)
    ans = 0
    for i in range(m+1):
        d = a[i+1] - a[i] - 1
        ans += (d + k - 1) // k
    return ans

if __name__ == '__main__':
    solve()