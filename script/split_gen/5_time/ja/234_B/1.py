def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
n=int(input())
points=[]
for i in range(n):
    x,y=map(int,input().split())
    points.append((x,y))
max_distance=0
for i in range(n):
    for j in range(i+1,n):
        distance=get_distance(points[i][0],points[i][1],points[j][0],points[j][1])
        if distance>max_distance:
            max_distance=distance
print(max_distance)
