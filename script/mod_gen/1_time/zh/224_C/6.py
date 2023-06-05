def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    # print(points)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                x3 = points[k][0]
                y3 = points[k][1]
                if (x1-x2)*(y1-y3) != (x1-x3)*(y1-y2):
                    count += 1
    print(count)

if __name__ == '__main__':
    main()