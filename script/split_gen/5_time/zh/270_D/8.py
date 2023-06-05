def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    a = [0] * (N + 1)
    for i in range(N):
        a[i] = 1
    for i in range(K):
        a[A[i]] = 0
    ans = 0
    for i in range(1, N + 1):
        if a[i] == 1:
            ans += 1
    print(ans)
