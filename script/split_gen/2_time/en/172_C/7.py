def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Asum = [0] * (N+1)
    Bsum = [0] * (M+1)
    for i in range(N):
        Asum[i+1] = Asum[i] + A[i]
    for i in range(M):
        Bsum[i+1] = Bsum[i] + B[i]
    ans = 0
    for i in range(N+1):
        if Asum[i] > K:
            break
        j = M
        while Asum[i] + Bsum[j] > K:
            j -= 1
        ans = max(ans, i + j)
    print(ans)
