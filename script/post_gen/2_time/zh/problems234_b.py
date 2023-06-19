Synthesizing 10/10 solutions

=======
Suggestion 1

def my_sqrt(x):
    ans = 1.0
    while abs(ans * ans - x) > 1e-10:
        ans = (ans + x / ans) / 2.0
    return ans

=======
Suggestion 2

def main():
    #读取输入
    n = int(input())
    points = []
    for i in range(n):
        x = int(input().split()[0])
        y = int(input().split()[1])
        points.append((x, y))
    #计算最大距离
    max_dist = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5
            if dist > max_dist:
                max_dist = dist
    #输出结果
    print(max_dist)

=======
Suggestion 3

def get_max_distance(x_list, y_list):
    distance_list = []
    for i in range(len(x_list)):
        for j in range(i,len(x_list)):
            distance_list.append((x_list[i]-x_list[j])**2 + (y_list[i]-y_list[j])**2)
    return max(distance_list)**(1/2)

=======
Suggestion 4

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

=======
Suggestion 5

def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

=======
Suggestion 6

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

=======
Suggestion 7

def maxDistance():
    N = int(input())
    pointList = []
    for i in range(N):
        pointList.append(list(map(int, input().split())))
    maxDistance = 0
    for i in range(N):
        for j in range(i+1, N):
            distance = (pointList[i][0]-pointList[j][0])**2 + (pointList[i][1]-pointList[j][1])**2
            if distance > maxDistance:
                maxDistance = distance
    print(maxDistance**0.5)

maxDistance()

=======
Suggestion 8

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))

max_distance = 0
for i in range(n):
    for j in range(i+1, n):
        max_distance = max(max_distance, distance(points[i][0], points[i][1], points[j][0], points[j][1]))

print(max_distance)

=======
Suggestion 9

def get_max_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            if distance > max_distance:
                max_distance = distance
    return max_distance

=======
Suggestion 10

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
