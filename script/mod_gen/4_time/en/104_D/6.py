def solve():
    S = input()
    mod = 10**9 + 7
    N = len(S)
    dp = [[[0]*3 for _ in range(3)] for _ in range(N)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(3):
            for k in range(3):
                if j == k == 0:
                    if S[i] == 'A' or S[i] == '?':
                        dp[i+1][1][0] += dp[i][0][0]
                    if S[i] == 'B' or S[i] == '?':
                        dp[i+1][0][1] += dp[i][0][0]
                    if S[i] == 'C' or S[i] == '?':
                        dp[i+1][0][0] += dp[i][0][0]
                elif j == 1 and k == 0:
                    if S[i] == 'A' or S[i] == '?':
                        dp[i+1][1][0] += dp[i][1][0]
                    if S[i] == 'B' or S[i] == '?':
                        dp[i+1][0][1] += dp[i][1][0]
                    if S[i] == 'C' or S[i] == '?':
                        dp[i+1][0][0] += dp[i][1][0]
                elif j == 0 and k == 1:
                    if S[i] == 'A' or S[i] == '?':
                        dp[i+1][1][1] += dp[i][0][1]
                    if S[i] == 'B' or S[i] == '?':
                        dp[i+1][0][1] += dp[i][0][1]
                    if S[i] == 'C' or S[i] == '?':
                        dp[i+1][0][0] += dp[i][0][1]
                elif j == 1 and k == 1:
                    if S[i] == 'A' or S[i] == '?':
                        dp[i+1][1][1] += dp[i][1][1]
                    if S[i] == 'B' or S[i] == '?':
                        dp[i+1][0][1] += dp[i][1][1]

if __name__ == '__main__':
    solve()