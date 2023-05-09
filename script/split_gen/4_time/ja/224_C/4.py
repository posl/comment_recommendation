def main():
    N = int(input())
    points = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                x3 = points[k][0]
                y3 = points[k][1]
                if (x1-x3)*(y2-y3) != (x2-x3)*(y1-y3):
                    count += 1
    print(count)
