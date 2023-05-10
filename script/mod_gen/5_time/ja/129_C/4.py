def solve():
    N,M = map(int,input().split())
    A = [0] * N
    for i in range(M):
        A[int(input())] = -1
    dp = [0] * N
    dp[0] = 1
    if A[1] != -1:
        dp[1] = 1
    for i in range(2,N):
        if A[i] == -1:
            continue
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
    print(dp[N-1])

if __name__ == '__main__':
    solve()