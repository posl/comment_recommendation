def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
max_distance = 0
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        d = distance(x1, y1, x2, y2)
        if d > max_distance:
            max_distance = d
print(max_distance)
