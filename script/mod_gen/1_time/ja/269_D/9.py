def main():
    #入力
    N = int(input())
    XY = [list(map(int,input().split())) for _ in range(N)]
    #連結成分の個数を数える
    ans = 0
    for i in range(N):
        if XY[i] == [-1,-1]:
            continue
        else:
            ans += 1
            #連結成分の中から、隣接するマスを探す
            XY[i] = [-1,-1]
            for j in range(N):
                if (XY[j][0] == XY[i][0] + 1 and XY[j][1] == XY[i][1]) or (XY[j][0] == XY[i][0] + 1 and XY[j][1] == XY[i][1] + 1) or (XY[j][0] == XY[i][0] and XY[j][1] == XY[i][1] - 1) or (XY[j][0] == XY[i][0] and XY[j][1] == XY[i][1] + 1) or (XY[j][0] == XY[i][0] - 1 and XY[j][1] == XY[i][1] - 1) or (XY[j][0] == XY[i][0] - 1 and XY[j][1] == XY[i][1]):
                    XY[j] = [-1,-1]
    print(ans)

if __name__ == '__main__':
    main()