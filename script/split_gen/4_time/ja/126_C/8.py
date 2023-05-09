def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i >= K:
            ans += 1
        else:
            tmp = 0
            while i < K:
                i *= 2
                tmp += 1
            ans += (1 / N) * (0.5 ** tmp)
    print(ans)
