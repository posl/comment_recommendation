def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = "No"
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x1 = xy[i][0]
                y1 = xy[i][1]
                x2 = xy[j][0]
                y2 = xy[j][1]
                x3 = xy[k][0]
                y3 = xy[k][1]
                if (x1 == x2 and x2 == x3) or (y1 == y2 and y2 == y3):
                    ans = "Yes"
    print(ans)

if __name__ == '__main__':
    main()