def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Asum = [0] * (N + 1)
    Bsum = [0] * (M + 1)
    for i in range(N):
        Asum[i + 1] = Asum[i] + A[i]
    for j in range(M):
        Bsum[j + 1] = Bsum[j] + B[j]
    ans = 0
    j = M
    for i in range(N + 1):
        if Asum[i] > K:
            break
        while Bsum[j] > K - Asum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

if __name__ == '__main__':
    main()