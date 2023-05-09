def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N - i, K - i) + 1):
            tmp = V[:i] + V[N - j:]
            tmp.sort()
            tmp = tmp[:K - i - j]
            ans = max(ans, sum(tmp))
    print(ans)
