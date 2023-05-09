def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Asum = [0]
    Bsum = [0]
    for i in range(N):
        Asum.append(Asum[-1]+A[i])
    for i in range(M):
        Bsum.append(Bsum[-1]+B[i])
    ans = 0
    j = M
    for i in range(N+1):
        if Asum[i] > K:
            break
        while Bsum[j] > K-Asum[i]:
            j -= 1
        ans = max(ans, i+j)
    print(ans)
