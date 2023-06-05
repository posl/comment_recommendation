def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int,input().split())))
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x1 = points[i][0] - points[j][0]
                y1 = points[i][1] - points[j][1]
                x2 = points[i][0] - points[k][0]
                y2 = points[i][1] - points[k][1]
                if x1*y2 != x2*y1:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()