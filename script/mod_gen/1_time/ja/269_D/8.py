def main():
    N = int(input())
    XY = [list(map(int,input().split())) for _ in range(N)]
    XY.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if XY[i][0] < XY[j][0] and XY[i][1] < XY[j][1]:
                if [XY[i][0]+XY[j][0],XY[i][1]+XY[j][1]] in XY:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()