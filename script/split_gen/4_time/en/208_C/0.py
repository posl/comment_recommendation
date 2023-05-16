def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    for i in range(N):
        ans[i] = K // N
        if i < K % N:
            ans[i] += 1
    for i in range(N):
        ans[i] += K // N * (a[i] - 1)
        if a[i] <= K % N:
            ans[i] += 1
    for i in range(N):
        print(ans[i])