def solve():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            if i == j:
                dp[i][j] = A[i]
            else:
                dp[i][j] = dp[i][j - 1] | A[j]
    ans = 0
    for i in range(N):
        for j in range(i, N):
            ans |= dp[i][j]
    print(ans)
solve()

if __name__ == '__main__':
    solve()