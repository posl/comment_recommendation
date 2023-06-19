def dist(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
n = int(input())
xy = []
for i in range(n):
    xy.append([int(x) for x in input().split()])
max_dist = 0
for i in range(n):
    for j in range(i+1, n):
        d = dist(xy[i][0], xy[i][1], xy[j][0], xy[j][1])
        if d > max_dist:
            max_dist = d
print(max_dist)
