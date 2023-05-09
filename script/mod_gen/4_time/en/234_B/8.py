def get_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
N = int(input())
points = []
for _ in range(N):
    points.append(tuple(map(int, input().split())))
max_distance = 0
for i in range(N):
    for j in range(i+1, N):
        distance = get_distance(points[i][0], points[i][1], points[j][0], points[j][1])
        if distance > max_distance:
            max_distance = distance
print(max_distance)

if __name__ == '__main__':
    get_distance()