def solve():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        score = i
        p = 1/N
        while score < K:
            score *= 2
            p /= 2
        ans += p
    print(ans)
