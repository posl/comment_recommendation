def solve():
    N, S = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # dp[i][j] = i枚目までのカードを使ってjを作れるか
    dp = [[False]*(S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if j >= A[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-A[i]]
            if j >= B[i]:
                dp[i+1][j] = dp[i+1][j] or dp[i][j-B[i]]
    if not dp[N][S]:
        print("No")
        return
    ans = ""
    i = N
    j = S
    while i > 0:
        if j >= A[i-1] and dp[i-1][j-A[i-1]]:
            ans = "H" + ans
            j -= A[i-1]
        else:
            ans = "T" + ans
            j -= B[i-1]
        i -= 1
    print("Yes")
    print(ans)

if __name__ == '__main__':
    solve()