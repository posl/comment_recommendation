def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            cnt = 0
            for k in range(N):
                if XY[i][0] == XY[j][0] == XY[k][0]:
                    cnt += 1
                elif (XY[j][1] - XY[i][1]) * (XY[k][0] - XY[i][0]) == (XY[k][1] - XY[i][1]) * (XY[j][0] - XY[i][0]):
                    cnt += 1
            ans += cnt * (cnt - 1) // 2
    print(ans)
