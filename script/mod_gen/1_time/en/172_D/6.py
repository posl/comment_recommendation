def solve(n):
    ans = 0
    for i in range(1, n+1):
        ans += i * (n//i) * (n//i+1) // 2
    return ans

if __name__ == '__main__':
    solve()