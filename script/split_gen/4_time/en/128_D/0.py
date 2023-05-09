def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) - l + 1):
            if l + r > N:
                break
            t = V[:l] + V[N - r:]
            t.sort()
            for i in range(min(K - l - r, l + r)):
                if t[i] < 0:
                    t[i] = 0
            ans = max(ans, sum(t))
    print(ans)
