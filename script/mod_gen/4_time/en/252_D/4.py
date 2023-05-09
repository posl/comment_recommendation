def solve(n, a):
    ans = 0
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    for i in range(n):
        ans += c[a[i]]
        c[a[i]] += b[a[i]]
        b[a[i]] += 1
    return ans

if __name__ == '__main__':
    solve()