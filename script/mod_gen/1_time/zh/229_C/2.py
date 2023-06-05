def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_a = max(A)
    max_b = max(B)
    if (max_a * max_b * N) < W:
        print(sum(A) * sum(B))
        return
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, -1, -1):
            if j >= B[i]:
                dp[j] = max(dp[j], dp[j - B[i]] + A[i])
    print(dp[W])

if __name__ == '__main__':
    main()