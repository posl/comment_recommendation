def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    #print(points)
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            #print("i = {}, j = {}".format(i, j))
            #print("points[i] = {}, points[j] = {}".format(points[i], points[j]))
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                continue
            #print("points[i][0] = {}, points[j][0] = {}, points[i][1] = {}, points[j][1] = {}".format(points[i][0], points[j][0], points[i][1], points[j][1]))
            if (points[i][0], points[j][1]) in points and (points[j][0], points[i][1]) in points:
                #print("points[i][0], points[j][1] = {}, points[j][0], points[i][1] = {}".format((points[i][0], points[j][1]), (points[j][0], points[i][1])))
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()