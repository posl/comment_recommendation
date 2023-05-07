def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    for m in range(1, 41):
        d = [1] * m
        for j in range(m):
            if XY[0][0] & (1 << j):
                d[j] = -1
        for i in range(1, N):
            for j in range(m):
                if (XY[i][0] - XY[i-1][0]) & (1 << j):
                    d[j] = -1
        for i in range(N):
            for j in range(m):
                if (XY[i][1] - XY[i-1][1]) & (1 << j):
                    d[j] = -1
        for i in range(N):
            for j in range(m):
                if (XY[i][0] - XY[i-1][0]) & (1 << j) and (XY[i][1] - XY[i-1][1]) & (1 << j):
                    d[j] = -1
        flag = True
        for i in range(N):
            for j in range(m):
                if (XY[i][0] - XY[i-1][0]) & (1 << j) and not (XY[i][1] - XY[i-1][1]) & (1 << j):
                    flag = False
                if not (XY[i][0] - XY[i-1][0]) & (1 << j) and (XY[i][1] - XY[i-1][1]) & (1 << j):
                    flag = False
        if flag:
            print(m)
            print(*d)
            for i in range(N):
                ans = []
                for j in range(m):
                    if (XY[i][0] - XY[i-1][0]) & (1 << j):
                        if (XY[i][0] - XY[i-1][0]) // d[j] > 0:
                            ans.append('R')
                        else:
                            ans.append('L')
                    elif (XY[i][1] - XY[i-1][1]) & (1 << j):
                        if (XY[i][1] - XY[i-1][1]) // d[j] > 0:
                            ans.append('U')
                        else:
                            ans.append('D

if __name__ == '__main__':
    solve()