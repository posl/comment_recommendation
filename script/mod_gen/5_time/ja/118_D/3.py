def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    match = [2,5,5,4,5,6,3,7,6]
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(N+1):
        for j in range(M):
            if i + match[A[j]-1] <= N:
                dp[i+match[A[j]-1]] = max(dp[i+match[A[j]-1]], dp[i]*10 + A[j])
    print(dp[N])

if __name__ == '__main__':
    solve()