def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i < K:
            ans += max(0, A[i] - X)
        else:
            ans += A[i]
    print(ans)
