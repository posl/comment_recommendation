def main():
    N, S = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[False] * (S + 1) for i in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(S + 1):
            if j >= A[i] and dp[i][j - A[i]]:
                dp[i + 1][j] = True
            if j >= B[i] and dp[i][j - B[i]]:
                dp[i + 1][j] = True
    if dp[N][S]:
        print('Yes')
        ans = []
        i = N
        j = S
        while i > 0:
            if j >= A[i - 1] and dp[i - 1][j - A[i - 1]]:
                ans.append('H')
                j -= A[i - 1]
            else:
                ans.append('T')
                j -= B[i - 1]
            i -= 1
        print(''.join(ans[::-1]))
    else:
        print('No')

if __name__ == '__main__':
    main()