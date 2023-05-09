def solve():
    n = int(input())
    xy = []
    for _ in range(n):
        xy.append(list(map(int, input().split())))
    xy.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if xy[i][0] == xy[j][0]:
                continue
            elif xy[i][1] <= xy[j][1] and xy[i][0] <= xy[j][0]:
                if (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) <= 1:
                    ans += 1
            elif xy[i][1] >= xy[j][1] and xy[i][0] >= xy[j][0]:
                if (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) >= 1:
                    ans += 1
            elif xy[i][1] >= xy[j][1] and xy[i][0] <= xy[j][0]:
                if (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) >= -1:
                    ans += 1
            elif xy[i][1] <= xy[j][1] and xy[i][0] >= xy[j][0]:
                if (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) <= -1:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    solve()