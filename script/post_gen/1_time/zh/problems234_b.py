Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    max_len = 0
    for i in range(n):
        for j in range(i+1, n):
            max_len = max(max_len, len_two_points(points[i], points[j]))
    print(max_len)

=======
Suggestion 2

def get_max_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            if distance > max_distance:
                max_distance = distance
    return max_distance ** 0.5

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    max_length = 0
    for i in range(N):
        for j in range(i+1,N):
            length = ((x[i]-x[j])**2+(y[i]-y[j])**2)**(1/2)
            if length > max_length:
                max_length = length
    print(max_length)

=======
Suggestion 4

def get_max_length(points):
    max_length = 0
    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            length = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            if length > max_length:
                max_length = length
    return max_length

=======
Suggestion 5

def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 6

def getDistance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

N = int(input())
points = []
for i in range(N):
    x,y = map(int,input().split())
    points.append((x,y))
maxDistance = 0
for i in range(N):
    for j in range(i+1,N):
        distance = getDistance(points[i][0],points[i][1],points[j][0],points[j][1])
        if distance > maxDistance:
            maxDistance = distance
print(maxDistance)

=======
Suggestion 7

def max_len(N, points):
    max_len = 0
    for i in range(N):
        for j in range(i+1, N):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            len = ((x1-x2)**2 + (y1-y2)**2)**0.5
            if len > max_len:
                max_len = len
    return max_len

=======
Suggestion 8

def maxDistance(x,y,n):
    max=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            distance=(x[i]-x[j])**2+(y[i]-y[j])**2
            if distance>max:
                max=distance
    return max**0.5

=======
Suggestion 9

def max_len(points):
    import math
    max_len = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x = points[i][0] - points[j][0]
            y = points[i][1] - points[j][1]
            length = math.sqrt(x**2 + y**2)
            if max_len < length:
                max_len = length
    return max_len

=======
Suggestion 10

def get_max_length(points):
    max_length = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            length = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5
            if length > max_length:
                max_length = length
    return max_length
