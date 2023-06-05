def area2(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])
n = int(input())
points = []
for i in range(n):
    points.append(tuple(map(int,input().split())))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if area2(points[i],points[j],points[k]) != 0:
                ans += 1
print(ans)
