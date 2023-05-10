def getDistances(start, points, distance):
    if len(points) == 0:
        return distance
    else:
        distances = []
        for i in range(len(points)):
            distances.append(getDistances(points[i], points[:i] + points[i+1:], distance + ((start[0] - points[i][0]) ** 2 + (start[1] - points[i][1]) ** 2) ** 0.5))
        return distances
N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
distances = []
for i in range(N):
    distances.append(getDistances(points[i], points[:i] + points[i+1:], 0))
sum = 0
for i in range(N):
    for j in range(len(distances[i])):
        sum += distances[i][j]
print(sum / (N * (N - 1)))

if __name__ == '__main__':
    getDistances()