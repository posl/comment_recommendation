def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Aの累積和
    Asum = [0]
    for i in range(N):
        Asum.append(A[i] + Asum[i])
    # Bの累積和
    Bsum = [0]
    for i in range(M):
        Bsum.append(B[i] + Bsum[i])
    # Aの累積和 + Bの累積和
    Csum = [0]
    for i in range(M):
        Csum.append(Bsum[i] + Asum[-1])
    # Bの累積和 + Aの累積和
    Dsum = [0]
    for i in range(N):
        Dsum.append(Asum[i] + Bsum[-1])
    # Aの累積和 + Bの累積和 と Bの累積和 + Aの累積和 のうち、K以下の最大値を求める
    ans = 0
    for i in range(N+1):
        if Asum[i] > K:
            break
        ans = max(ans, i + bisect.bisect_right(Csum, K-Asum[i])-1)
    for i in range(M+1):
        if Bsum[i] > K:
            break
        ans = max(ans, i + bisect.bisect_right(Dsum, K-Bsum[i])-1)
    print(ans)
