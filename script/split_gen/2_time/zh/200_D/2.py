def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    dp = [[0]*(200) for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(200):
            dp[i][j] = dp[i-1][j]
        dp[i][A[i]%200] = 1
        for j in range(200):
            dp[i][(j+A[i])%200] |= dp[i-1][j]
    for i in range(200):
        if dp[N][i] and dp[N][(i+1)%200]:
            B = []
            C = []
            for j in range(N, 0, -1):
                if dp[j-1][i]:
                    B.append(j)
                    i = (i-A[j])%200
                elif dp[j-1][(i+200-A[j])%200]:
                    C.append(j)
                    i = (i-A[j]+200)%200
            print('Yes')
            print(len(B), ' '.join(map(str, B)))
            print(len(C), ' '.join(map(str, C)))
            return
    print('No')
solve()
