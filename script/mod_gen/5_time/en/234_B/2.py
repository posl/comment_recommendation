def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
max_distance = 0
for i in range(N):
    for j in range(i+1, N):
        max_distance = max(max_distance, distance(points[i][0], points[i][1], points[j][0], points[j][1]))
print(max_distance)

if __name__ == '__main__':
    distance()