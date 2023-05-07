def main():
    S = input()
    atcoder = "atcoder"
    dp = [[0 for _ in range(len(S)+1)] for _ in range(len(atcoder)+1)]
    for i in range(len(S)):
        for j in range(len(atcoder)):
            if S[i] == atcoder[j]:
                dp[j+1][i+1] = dp[j][i] + 1
            else:
                dp[j+1][i+1] = dp[j+1][i]
        dp[j+1][i+1] += dp[j+1][i]
    print(len(S) - dp[-1][-1])
