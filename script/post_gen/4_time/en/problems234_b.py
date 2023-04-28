Synthesizing 10/10 solutions

=======
Suggestion 1

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

=======
Suggestion 2

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

=======
Suggestion 3

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

=======
Suggestion 4

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

N = int(input())
points = []
for i in range(N):
    points.append(list(map(int, input().split())))

max_distance = 0
for i in range(N):
    for j in range(i+1, N):
        max_distance = max(max_distance, distance(points[i][0], points[i][1], points[j][0], points[j][1]))

print(max_distance)

=======
Suggestion 5

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i+1, N):
        d = distance(points[i][0], points[i][1], points[j][0], points[j][1])
        if d > ans:
            ans = d
print(ans)

=======
Suggestion 6

def main():
    import math
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    max_len = 0
    for i in range(n):
        for j in range(i+1, n):
            len = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if len > max_len:
                max_len = len
    print(max_len)

=======
Suggestion 7

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

N = int(input())
x = []
y = []
for i in range(N):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

max_distance = 0
for i in range(N):
    for j in range(i+1,N):
        dist = distance(x[i],y[i],x[j],y[j])
        if dist > max_distance:
            max_distance = dist

print(max_distance)

=======
Suggestion 8

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

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

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    import math
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans,math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2))
    print(ans)
