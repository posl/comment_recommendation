def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append([x, y])
    ans = 0
    for i in range(N):
        for j in range(N):
            if XY[i][0] == XY[j][0] or XY[i][1] == XY[j][1]:
                continue
            for k in range(N):
                if XY[i][0] == XY[k][0] or XY[i][1] == XY[k][1]:
                    continue
                if XY[j][0] == XY[k][0] or XY[j][1] == XY[k][1]:
                    continue
                if XY[i][0] == XY[j][0] and XY[j][0] == XY[k][0]:
                    ans += 1
                elif XY[i][1] == XY[j][1] and XY[j][1] == XY[k][1]:
                    ans += 1
    print(ans//2)
