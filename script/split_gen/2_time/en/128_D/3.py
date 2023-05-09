def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for a in range(min(N, K) + 1):
        for b in range(min(N - a, K - a) + 1):
            if a + b > K:
                continue
            v = V[:a] + V[N - b:]
            v.sort()
            for c in range(min(a + b, K - a - b)):
                if v[c] >= 0:
                    break
                v[c] = 0
            ans = max(ans, sum(v))
    print(ans)
