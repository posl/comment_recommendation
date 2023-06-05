def getArea(x1, y1, x2, y2, x3, y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
count = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if getArea(x1, y1, x2, y2, x3, y3) != 0:
                count += 1
print(count)
