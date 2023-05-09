def solve():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                x3 = points[k][0]
                y3 = points[k][1]
                if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
                    continue
                ans += 1
    print(ans)

if __name__ == '__main__':
    solve()