def main():
    N, S = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [[False] * (S+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S+1):
            if dp[i][j]:
                dp[i+1][j] = True
                if j + a[i] <= S:
                    dp[i+1][j+a[i]] = True
                if j + b[i] <= S:
                    dp[i+1][j+b[i]] = True
    if dp[N][S]:
        print("Yes")
        ans = ""
        i = N
        j = S
        while i > 0:
            if j - a[i-1] >= 0 and dp[i-1][j-a[i-1]]:
                ans = "H" + ans
                j -= a[i-1]
            else:
                ans = "T" + ans
                j -= b[i-1]
            i -= 1
        print(ans)
    else:
        print("No")
