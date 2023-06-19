def get_area(x1,y1,x2,y2,x3,y3):
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split())))
points.sort()
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            temp = get_area(points[i][0],points[i][1],points[j][0],points[j][1],points[k][0],points[k][1])
            if temp > ans:
                ans = temp
print(ans)
