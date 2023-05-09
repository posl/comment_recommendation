def solve():
    S = input()
    atcoder = "atcoder"
    dp = [[0 for _ in range(len(atcoder)+1)] for _ in range(len(S)+1)]
    for i in range(len(S)+1):
        dp[i][0] = i
    for i in range(len(atcoder)+1):
        dp[0][i] = i
    for i in range(1, len(S)+1):
        for j in range(1, len(atcoder)+1):
            if S[i-1] == atcoder[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j]+1, # delete
                    dp[i][j-1]+1, # insert
                    dp[i-1][j-1]+1 # replace
                )
    print(dp[len(S)][len(atcoder)])
    return 0
