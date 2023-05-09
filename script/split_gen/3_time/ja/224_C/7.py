def main():
    n = int(input())
    xy = [list(map(int,input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x1 = xy[i][0]
                y1 = xy[i][1]
                x2 = xy[j][0]
                y2 = xy[j][1]
                x3 = xy[k][0]
                y3 = xy[k][1]
                if (x2-x1)*(y3-y1) != (x3-x1)*(y2-y1):
                    ans += 1
    print(ans)
