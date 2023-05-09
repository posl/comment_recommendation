def solve(n):
    ans = 0
    i = 1
    while i <= n:
        ans += n // i
        i *= 10
    return ans
n = int(input())
print(solve(n) % 998244353)

if __name__ == '__main__':
    solve()