def main():
    S = input()
    ABC = [0, 0, 0]
    ABC[0] = S.count('A')
    ABC[1] = S.count('B')
    ABC[2] = S.count('C')
    Q = S.count('?')
    mod = 10**9 + 7
    #print(ABC, Q)
    dp = [[0] * 4 for _ in range(Q+1)]
    dp[0][3] = 1
    #print(dp)
    for i in range(Q):
        for j in range(4):
            dp[i+1][j] = dp[i][j] * 2
            dp[i+1][j] %= mod
        for j in range(3):
            dp[i+1][j] += dp[i][3]
            dp[i+1][j] %= mod
        dp[i+1][3] += dp[i][3]
        dp[i+1][3] %= mod
    #print(dp)
    ans = 0
    for i in range(3):
        ans += dp[Q][i] * ABC[i]
        ans %= mod
    ans += dp[Q][3]
    ans %= mod
    print(ans)
