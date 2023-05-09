def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            v = sorted(V[:i] + V[N - j:])
            for k in range(min(i + j, K - i - j)):
                if v[k] < 0:
                    v[k] = 0
            ans = max(ans, sum(v))
    print(ans)
