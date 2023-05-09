def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i - 1 for i in A]
    if N == K:
        print(1)
        return
    if K == 2:
        print((N + 1) // 2)
        return
    # dp[i][j] := i回目の操作で、j番目の要素が1番目に持ってくる要素になるまでの操作回数
    dp = [[0] * N for _ in range(2)]
    for i in range(N):
        dp[0][i] = (i + 1) // K + (i + K) // K
    for i in range(1, N):
        dp[1][i] = dp[0][A[i]] + dp[1][A[i]]
    print((dp[1][0] + 1) // 2)
main()

if __name__ == '__main__':
    main()