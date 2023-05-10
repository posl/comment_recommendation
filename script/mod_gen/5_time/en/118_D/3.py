def solve(n, m, a):
    dp = [-float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(m):
            if i - a[j][1] >= 0:
                dp[i] = max(dp[i], dp[i - a[j][1]] + a[j][0])
    return dp[-1]
n, m = map(int, input().split())
a = []
for i, v in enumerate(map(int, input().split())):
    a.append((v, i + 1))
a.sort(reverse=True)
print(solve(n, m, a))

if __name__ == '__main__':
    solve()