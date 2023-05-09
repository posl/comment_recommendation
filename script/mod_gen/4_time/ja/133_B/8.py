def getDistance(x, y):
    dist = 0
    for i in range(len(x)):
        dist += (x[i] - y[i]) ** 2
    return dist ** 0.5
n, d = map(int, input().split())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if getDistance(points[i], points[j]).is_integer():
            ans += 1
print(ans)

if __name__ == '__main__':
    getDistance()