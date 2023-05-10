def main():
    #input
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #compute
    sumP = [0] * (N + 1)
    for i in range(N):
        sumP[i + 1] = sumP[i] + P[i]
    ans = 0
    for i in range(K, N + 1):
        ans = max(ans, (sumP[i] - sumP[i - K]) / 2 + sumP[i - K])
    print(ans)
