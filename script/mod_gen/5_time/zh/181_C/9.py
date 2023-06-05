def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    #print(points)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                #print(points[i], points[j], points[k])
                if (points[j][1] - points[i][1]) * (points[k][0] - points[i][0]) == (points[k][1] - points[i][1]) * (points[j][0] - points[i][0]):
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    main()