Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] * 10 % MOD
    ans = dp[N] - (dp[N // 2] + dp[(N + 1) // 2]) % MOD
    if ans < 0:
        ans += MOD
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[0]*10 for _ in range(N+1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[N])%MOD)

=======
Suggestion 3

def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[0]*10 for _ in range(N+1)]
    dp[1] = [1]*10
    for i in range(2,N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        for j in range(1,9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[N])%MOD)

=======
Suggestion 4

def main():
    n = int(input())
    mod = 10**9 + 7
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] * 10 + 1) % mod
    print((dp[n] * 2 - 1) % mod)

=======
Suggestion 5

def main():
    N = int(input())
    dp = [[0,0,0] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        dp[i][0] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%1000000007
        dp[i][1] = (dp[i-1][0]+dp[i-1][2])%1000000007
        dp[i][2] = (dp[i-1][0]+dp[i-1][1])%1000000007
    print((dp[N][0]+dp[N][1]+dp[N][2])%1000000007)

=======
Suggestion 6

def main():
    N=int(input())
    MOD=10**9+7
    ans=0
    for i in range(1,N+1):
        ans+=pow(10,i,MOD)*pow(9,i,MOD)*pow(8,MOD-2,MOD)*pow(8,N-i,MOD)
        ans%=MOD
    print(ans)
main()

=======
Suggestion 7

def main():
    n = int(input())
    mod = 10**9 + 7
    ans = 0
    for i in range(1, n + 1):
        ans += i * pow(10, i, mod) * pow(9, n - i, mod)
        ans %= mod
    print(ans)

=======
Suggestion 8

def solve(n):
    return (pow(10,n,mod) - 2*pow(9,n,mod) + pow(8,n,mod))%mod

=======
Suggestion 9

def main():
    N = int(input())
    MOD = 10**9 + 7
    ans = 0
    for i in range(1, N+1):
        ans += 2 * (10**i - 9**i) + 8**i
    print(ans % MOD)

=======
Suggestion 10

def solve(N):
    # dp[i][j][k] = i桁目まで見て、0が出現したか、9が出現したか、その他の数字が出現したか
    # 0: 未出現
    # 1: 出現済み
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(2):
            for k in range(3):
                for l in range(10):
                    if l == 0:
                        dp[i+1][1][k] += dp[i][j][k]
                    elif l == 9:
                        dp[i+1][j][2] += dp[i][j][k]
                    else:
                        dp[i+1][j][1] += dp[i][j][k]
    ans = 0
    for j in range(2):
        for k in range(3):
            ans += dp[N][j][k]
    return ans % (10**9+7)
