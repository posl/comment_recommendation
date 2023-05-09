def main():
    N, S = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(1, N + 1):
        for j in range(S + 1):
            if j >= A[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - A[i - 1]]
            if j >= B[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - B[i - 1]]
    if dp[N][S]:
        print("Yes")
        ans = []
        i = N
        j = S
        while i > 0:
            if j >= A[i - 1] and dp[i - 1][j - A[i - 1]]:
                ans.append("H")
                j -= A[i - 1]
            else:
                ans.append("T")
                j -= B[i - 1]
            i -= 1
        print("".join(ans[::-1]))
    else:
        print("No")

if __name__ == '__main__':
    main()