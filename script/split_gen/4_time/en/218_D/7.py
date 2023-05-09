def main():
    N = int(input())
    points = []
    for i in range(N):
        point = list(map(int, input().split()))
        points.append(point)
    points.sort()
    #print(points)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if points[i][0] < points[j][0] and points[i][1] < points[j][1]:
                if [points[i][0], points[j][1]] in points and [points[j][0], points[i][1]] in points:
                    count += 1
    print(count)
