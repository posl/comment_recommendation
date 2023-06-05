def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(K, N) + 1):
        for r in range(min(K, N) + 1 - l):
            a = V[:l] + V[N - r:]
            a.sort()
            ans = max(ans, sum(a[max(0, K - l - r):]))
    print(ans)
main()
