def solve():
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (xy[i][1] - xy[j][1]) / (xy[i][0] - xy[j][0]) <= 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()