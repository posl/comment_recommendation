def solve():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(K, N) + 1):
        for j in range(min(K, N) - i + 1):
            left = V[:i]
            right = V[N - j:]
            new = left + right
            new.sort()
            new.reverse()
            for k in range(min(K - i - j, len(new))):
                if new[k] < 0:
                    new[k] = 0
            ans = max(ans, sum(new))
    print(ans)
solve()
