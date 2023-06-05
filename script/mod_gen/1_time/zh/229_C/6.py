def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, B[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - B[i]] + A[i])
    print(dp[W])

if __name__ == '__main__':
    main()