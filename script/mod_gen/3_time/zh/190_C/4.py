def solve():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    CD = [tuple(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2 ** K):
        balls = [0] * N
        for j, (c, d) in enumerate(CD):
            if (i >> j) & 1:
                balls[c - 1] += 1
            else:
                balls[d - 1] += 1
        cnt = 0
        for a, b in AB:
            if balls[a - 1] >= 1 and balls[b - 1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
solve()
