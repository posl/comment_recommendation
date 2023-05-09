def solve():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                x3 = points[k][0]
                y3 = points[k][1]
                if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    solve()