def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(K, N) + 1):
        for r in range(min(K, N) - l + 1):
            if l + r > N:
                continue
            A = sorted(V[:l] + V[N - r:])
            ans = max(ans, sum(A[max(0, K - l - r):]))
    print(ans)
