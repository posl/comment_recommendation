def main():
    N = int(input())
    xy = [[int(i) for i in input().split()] for _ in range(N)]
    xy.sort()
    #print(xy)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                x1 = xy[j][0] - xy[i][0]
                y1 = xy[j][1] - xy[i][1]
                x2 = xy[k][0] - xy[i][0]
                y2 = xy[k][1] - xy[i][1]
                if x1*y2 - x2*y1 != 0:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()