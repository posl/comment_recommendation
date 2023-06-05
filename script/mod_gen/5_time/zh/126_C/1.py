def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1
        else:
            p = 1
            while i < K:
                i *= 2
                p /= 2
            ans += p
    print(ans / N)
solve()
