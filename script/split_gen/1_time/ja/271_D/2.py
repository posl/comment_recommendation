def main():
    N, S = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[False] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = dp[i][j] | dp[i][j - A[i]]
            else:
                dp[i + 1][j] = dp[i][j]
            if j - B[i] >= 0:
                dp[i + 1][j] = dp[i][j] | dp[i][j - B[i]]
            else:
                dp[i + 1][j] = dp[i][j]
    if dp[N][S]:
        print('Yes')
        ans = []
        for i in range(N - 1, -1, -1):
            if S - A[i] >= 0:
                if dp[i][S - A[i]]:
                    ans.append('H')
                    S -= A[i]
                    continue
            if S - B[i] >= 0:
                if dp[i][S - B[i]]:
                    ans.append('T')
                    S -= B[i]
                    continue
        print(''.join(ans[::-1]))
    else:
        print('No')
