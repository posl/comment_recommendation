def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            if i + j == 0:
                continue
            v = V[:i] + V[N - j:]
            v.sort()
            for k in range(min(K - i - j, len(v))):
                if v[k] < 0:
                    v[k] = 0
                else:
                    break
            ans = max(ans, sum(v))
    print(ans)
