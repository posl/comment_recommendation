def solve():
    N, S = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] |= dp[i][j - A[i]]
            if j - B[i] >= 0:
                dp[i + 1][j] |= dp[i][j - B[i]]
    if dp[N][S]:
        print("Yes")
        i = N
        j = S
        ans = ""
        while i > 0:
            if j - A[i - 1] >= 0 and dp[i - 1][j - A[i - 1]]:
                ans += "H"
                j -= A[i - 1]
            else:
                ans += "T"
                j -= B[i - 1]
            i -= 1
        print(ans[::-1])
    else:
        print("No")

if __name__ == '__main__':
    solve()