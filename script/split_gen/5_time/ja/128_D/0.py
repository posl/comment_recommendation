def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) - l + 1):
            gems = V[:l] + V[N - r:]
            gems.sort()
            tmp = sum(gems)
            for i in range(min(K - l - r, l + r)):
                if gems[i] < 0:
                    tmp -= gems[i]
            ans = max(ans, tmp)
    print(ans)
