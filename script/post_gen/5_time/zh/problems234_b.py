Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def maxDistance(points):
    ans = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ans = max(ans, distance(points[i], points[j]))
    return ans

=======
Suggestion 2

def problem234_b():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    max_length = 0
    for i in range(n):
        for j in range(i+1, n):
            length = ((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)**0.5
            if length > max_length:
                max_length = length
    print(max_length)

problem234_b()

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, ((x[i]-x[j])**2+(y[i]-y[j])**2)**(1/2))
    print(ans)

=======
Suggestion 4

def max_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5
            if distance > max_distance:
                max_distance = distance
    return max_distance

=======
Suggestion 5

def get_max_len(points):
    max_len = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x = points[i][0] - points[j][0]
            y = points[i][1] - points[j][1]
            d = x*x + y*y
            if d > max_len:
                max_len = d
    return max_len

=======
Suggestion 6

def getDistance(point1, point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5

=======
Suggestion 7

def distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

n = int(input())
points = []
for i in range(n):
    points.append([int(x) for x in input().split()])

ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans = max(ans, distance(points[i], points[j]))

print(ans)

=======
Suggestion 8

def get_max_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
            if distance > max_distance:
                max_distance = distance
    return max_distance**0.5

=======
Suggestion 9

def max_len(n, points):
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n):
            len = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            if len > max_len:
                max_len = len
    return max_len ** 0.5
