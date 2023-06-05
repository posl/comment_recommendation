def solve():
    N, S = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
                if j + A[i][0] <= S:
                    dp[i + 1][j + A[i][0]] = True
                if j + A[i][1] <= S:
                    dp[i + 1][j + A[i][1]] = True
    if dp[N][S]:
        print("Yes")
        ans = ["T"] * N
        i = N - 1
        j = S
        while i >= 0:
            if j - A[i][0] >= 0 and dp[i][j - A[i][0]]:
                ans[i] = "H"
                j -= A[i][0]
            elif j - A[i][1] >= 0 and dp[i][j - A[i][1]]:
                ans[i] = "T"
                j -= A[i][1]
            else:
                assert False
            i -= 1
        print("".join(ans))
    else:
        print("No")
solve()
