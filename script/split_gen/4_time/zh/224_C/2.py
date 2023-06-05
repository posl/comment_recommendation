def getArea(x1,y1,x2,y2,x3,y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split())))
count = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            x3 = points[k][0]
            y3 = points[k][1]
            if getArea(x1,y1,x2,y2,x3,y3) != 0:
                count += 1
print(count)
