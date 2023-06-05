def main():
    A,B,K = map(int,input().split())
    S = A+B
    dp = [[0 for _ in range(B+1)] for _ in range(A+1)]
    dp[0][0] = 1
    for i in range(A+1):
        for j in range(B+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    ans = ""
    while A+B > 0:
        if A == 0:
            ans += "b"
            B -= 1
        elif B == 0:
            ans += "a"
            A -= 1
        elif K <= dp[A-1][B]:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= dp[A-1][B]
            B -= 1
    print(ans)
