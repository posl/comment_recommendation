def solve(n, a):
    ans = 0
    for i in range(n):
        ans += a[i]
    ans = 360 - ans
    return ans

if __name__ == '__main__':
    solve()