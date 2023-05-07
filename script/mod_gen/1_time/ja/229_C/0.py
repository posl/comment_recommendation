def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A_max = max(A)
    A_min = min(A)
    B_max = max(B)
    if A_max < B_max:
        print(0)
        return
    if N == 1:
        print(A[0] * min(B[0], W))
        return
    limit = A_max * W
    dp = [0] * (limit + 1)
    for i in range(N):
        for j in range(limit, A[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - A[i]] + B[i])
    ans = 0
    for i in range(W + 1):
        ans = max(ans, dp[i])
    print(ans)

if __name__ == '__main__':
    main()