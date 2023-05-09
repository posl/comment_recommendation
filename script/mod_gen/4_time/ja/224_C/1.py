def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x1 = xy[i][0] - xy[k][0]
                y1 = xy[i][1] - xy[k][1]
                x2 = xy[j][0] - xy[k][0]
                y2 = xy[j][1] - xy[k][1]
                if x1*y2 - x2*y1 != 0:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()