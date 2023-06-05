def distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
n = int(input())
points = []
for i in range(n):
    points.append([int(x) for x in input().split()])
ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans = max(ans, distance(points[i], points[j]))
print(ans)
