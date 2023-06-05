def solve():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(2 ** k):
        balls = [0] * n
        for j in range(k):
            if (i >> j) & 1:
                balls[cd[j][0]-1] += 1
            else:
                balls[cd[j][1]-1] += 1
        cnt = 0
        for a, b in ab:
            if balls[a-1] > 0 and balls[b-1] > 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)
solve()
