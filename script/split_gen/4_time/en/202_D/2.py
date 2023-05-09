def main():
    A, B, K = map(int, input().split())
    dp = [[0 for _ in range(B+1)] for _ in range(A+1)]
    dp[0][0] = 1
    for i in range(A+1):
        for j in range(B+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    ans = ''
    while A > 0 and B > 0:
        if K <= dp[A-1][B]:
            ans += 'a'
            A -= 1
        else:
            ans += 'b'
            K -= dp[A-1][B]
            B -= 1
    ans += 'a' * A
    ans += 'b' * B
    print(ans)
