def solve(n, a):
    ans = 0
    for i in range(1, n):
        if a[i] > a[i - 1]:
            ans += 1
    return (ans + 1) * 2

if __name__ == '__main__':
    solve()