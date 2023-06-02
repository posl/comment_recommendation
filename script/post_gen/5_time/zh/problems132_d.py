Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    dp[0][0] = 1
    for i in range(1,k+1):
        for j in range(n+1):
            if j < i:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i][j-1] * (i+1)) % mod
    print(dp[k][n])

=======
Suggestion 2

def problems132_d():
    pass

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    #计算组合数
    def comb(n, r, mod=10**9+7):
        if r == 0 or r == n:
            return 1
        if r == 1:
            return n
        if r > n:
            return 0
        if r > n - r:  # 5C3 = 5C2
            return comb(n, n - r, mod)
        return comb(n - 1, r - 1) + comb(n - 1, r)

    #计算组合数的和
    def combsum(n, r, mod=10**9+7):
        if r == 0 or r == n:
            return 1
        if r == 1:
            return (n+1)*n//2
        if r > n:
            return 0
        if r > n - r:  # 5C3 = 5C2
            return combsum(n, n - r, mod)
        return combsum(n - 1, r - 1) + combsum(n - 1, r)
    #计算组合数的乘积
    def combmulti(n, r, mod=10**9+7):
        if r == 0 or r == n:
            return 1
        if r == 1:
            return n
        if r > n:
            return 0
        if r > n - r:  # 5C3 = 5C2
            return combmulti(n, n - r, mod)
        return combmulti(n - 1, r - 1) * combmulti(n - 1, r)
    #计算组合数的除法
    def combdiv(n, r, mod=10**9+7):
        if r == 0 or r == n:
            return 1
        if r == 1:
            return n
        if r > n:
            return 0
        if r > n - r:  # 5C3 = 5C2
            return combdiv(n, n - r, mod)
        return combdiv(n - 1, r - 1) // combdiv

=======
Suggestion 4

def problems132_d():
    n,k = map(int,input().split())
    mod = 10**9+7
    ans = [0]*k
    for i in range(1,k+1):
        if i == 1:
            ans[i-1] = n-k+1
        else:
            ans[i-1] = (n-k+1)*(i-1)*(n-k+2-i)//(i*(i-1))%mod
    for i in range(k):
        print(ans[i])

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    #dp[i]表示i步走到第i个格子的走法
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] = dp[i-1]*2
        if i-k>=0:
            dp[i] -= dp[i-k]
        dp[i] %= mod
    #print(dp)
    #s[i]表示前i步走到第i个格子的走法
    s = [0]*(n+1)
    for i in range(1,n+1):
        s[i] = s[i-1]+dp[i]
        s[i] %= mod
    #print(s)
    ans = [0]*k
    for i in range(1,k+1):
        ans[i-1] = (s[n]-s[n-i])%mod
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    print("hello world")
    return

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    #初始化
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    dp[0][0] = 1
    #动态规划
    for i in range(1,k+1):
        for j in range(n+1):
            if j-i >= 0:
                dp[i][j] = (dp[i-1][j]+dp[i][j-1])%mod
            else:
                dp[i][j] = dp[i-1][j]
    #输出
    for i in range(1,k+1):
        print(dp[i][n]-dp[i-1][n])

=======
Suggestion 8

def mod(x):
    return x % (10**9 + 7)

n, k = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1
for i in range(k):
    for j in range(n + 1):
        dp[i + 1][j] = mod(dp[i + 1][j] + dp[i][j])
        dp[i + 1][j] = mod(dp[i + 1][j] + dp[i][j] * (n - j))
        if j + 1 <= n:
            dp[i + 1][j + 1] = mod(dp[i + 1][j + 1] + dp[i][j] * j)
print(dp[k][n])
for i in range(k):
    print(dp[i + 1][n])

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(i+1):
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
            dp[i][j] += dp[i-1][j] * (i-j)
            dp[i][j] %= 10**9+7
    for i in range(1, K+1):
        print(dp[N][i])
main()
