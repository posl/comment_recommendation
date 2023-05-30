def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
max_distance = 0
for i in range(n):
    for j in range(i+1,n):
        d = distance(points[i], points[j])
        if max_distance < d:
            max_distance = d
print(max_distance)
