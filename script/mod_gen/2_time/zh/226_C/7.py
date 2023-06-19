def solve(n, t, k, a):
    #print(n, t, k, a)
    dp = [0] * (n+1)
    for i in range(n):
        for j in range(k[i]):
            dp[a[i][j]] = max(dp[a[i][j]], dp[i+1] + t[i])
    print(max(dp))
n = int(input())
t = []
k = []
a = []
for i in range(n):
    t_, k_ = map(int, input().split())
    t.append(t_)
    k.append(k_)
    a.append(list(map(int, input().split())))
solve(n, t, k, a)
