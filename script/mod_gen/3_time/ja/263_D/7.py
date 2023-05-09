def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #A = [0] + A + [0]
    #N += 2
    #dp = [[0] * (N+1) for _ in range(N+1)]
    #dp[0][0] = sum(A)
    #for i in range(N):
    #    for j in range(i+1):
    #        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + L)
    #        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + R)
    #print(max(dp[N]))
    A.sort()
    ans = 0
    for i in range(N):
        if i < N/2:
            ans += L
        else:
            ans += R
    print(ans)

if __name__ == '__main__':
    main()