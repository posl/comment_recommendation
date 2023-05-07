def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    for i in range(N):
        if K >= N - i:
            ans[i] = a[i] + (K - (N - i)) // N
            K -= (K - (N - i)) // N * N
        else:
            ans[i] = a[i]
    for i in range(K):
        ans[i] += 1
    for i in range(N):
        print(ans[i])
