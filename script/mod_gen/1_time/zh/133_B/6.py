def getDistance(p1, p2):
    D = len(p1)
    sum = 0
    for i in range(D):
        sum += (p1[i] - p2[i]) ** 2
    return sum ** 0.5
N, D = map(int, input().split())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))
count = 0
for i in range(N):
    for j in range(i+1, N):
        if getDistance(points[i], points[j]).is_integer():
            count += 1
print(count)

if __name__ == '__main__':
    getDistance()