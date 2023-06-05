def main():
    A, B, K = map(int, raw_input().strip().split())
    S = A+B
    dp = [[0 for i in range(B+1)] for j in range(A+1)]
    dp[0][0] = 1
    for i in range(1, A+1):
        dp[i][0] = 1
        for j in range(1, B+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    ans = ""
    while A+B > 0:
        if A == 0:
            ans += "b"
            B -= 1
            continue
        if B == 0:
            ans += "a"
            A -= 1
            continue
        if dp[A-1][B] >= K:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= dp[A-1][B]
            B -= 1
    print ans

if __name__ == '__main__':
    main()