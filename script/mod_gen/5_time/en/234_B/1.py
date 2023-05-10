def dist(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
n = int(input())
points = [list(map(int, input().split())) for i in range(n)]
max_dist = 0
for i in range(n):
    for j in range(i+1, n):
        max_dist = max(max_dist, dist(points[i][0], points[i][1], points[j][0], points[j][1]))
print(max_dist)

if __name__ == '__main__':
    dist()