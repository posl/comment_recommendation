def solve():
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    xy = sorted(xy)
    xy = [(x - xy[0][0], y - xy[0][1]) for x, y in xy]
    xy = [xy[0]] + [(x - xy[0][0], y - xy[0][1]) for x, y in xy[1:]]
    xy = sorted(xy, key=lambda x: x[1] / x[0])
    xy = [(x, y) for x, y in xy if x != 0 or y != 0]
    n = len(xy)
    if n == 1:
        print(1)
        return
    ans = n
    for i in range(n):
        for j in range(i + 1, n):
            a = xy[j][0] - xy[i][0]
            b = xy[j][1] - xy[i][1]
            cnt = 0
            for k in range(n):
                for l in range(k + 1, n):
                    if xy[l][0] - xy[k][0] == a and xy[l][1] - xy[k][1] == b:
                        cnt += 1
            ans = min(ans, n - cnt)
    print(ans)
solve()
