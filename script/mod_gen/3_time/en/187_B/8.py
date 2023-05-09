def check_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope >= -1 and slope <= 1
n = int(input())
points = []
for i in range(n):
    points.append(tuple(map(int, input().split())))
count = 0
for i in range(n):
    for j in range(i+1, n):
        if check_slope(points[i][0], points[i][1], points[j][0], points[j][1]):
            count += 1
print(count)

if __name__ == '__main__':
    check_slope()