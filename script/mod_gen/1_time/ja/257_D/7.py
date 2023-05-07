def main():
    N = int(input())
    xyp = [list(map(int, input().split())) for _ in range(N)]
    INF = 10**18
    ans = INF
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if i == k or j == k:
                    continue
                if xyp[i][2]*xyp[j][2] < abs(xyp[i][0]-xyp[j][0])+abs(xyp[i][1]-xyp[j][1]):
                    continue
                if xyp[j][2]*xyp[k][2] < abs(xyp[j][0]-xyp[k][0])+abs(xyp[j][1]-xyp[k][1]):
                    continue
                if xyp[k][2]*xyp[i][2] < abs(xyp[k][0]-xyp[i][0])+abs(xyp[k][1]-xyp[i][1]):
                    continue
                ans = min(ans, xyp[i][2]+xyp[j][2]+xyp[k][2])
    if ans == INF:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()