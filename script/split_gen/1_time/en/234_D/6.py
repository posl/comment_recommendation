def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(1, N):
        P[i] += P[i-1]
    ans = 0
    for i in range(K-1, N):
        if i == K-1:
            ans = max(ans, P[i])
        else:
            ans = max(ans, P[i] - P[i-K])
    print(ans)
