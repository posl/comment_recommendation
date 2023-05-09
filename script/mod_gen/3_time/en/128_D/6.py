def problem():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            jewels = V[:i] + V[N-j:]
            jewels.sort()
            for k in range(min(K-i-j, len(jewels))):
                if jewels[k] < 0:
                    jewels[k] = 0
            ans = max(ans, sum(jewels))
    print(ans)
problem()

if __name__ == '__main__':
    problem()