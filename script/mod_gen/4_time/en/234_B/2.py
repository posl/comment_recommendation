def distance(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
max_distance = 0
for i in range(n):
    for j in range(i+1, n):
        max_distance = max(max_distance, distance(points[i], points[j]))
print(max_distance)

if __name__ == '__main__':
    distance()