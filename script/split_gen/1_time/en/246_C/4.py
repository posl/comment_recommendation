def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(N):
        if i < K:
            ans += max(A[i] - X, 0)
        else:
            ans += A[i]
    print(ans)
