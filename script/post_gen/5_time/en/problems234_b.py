Synthesizing 10/10 solutions

=======
Suggestion 1

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int, input().split())))

max_distance = 0
for i in range(n):
    for j in range(i+1,n):
        d = distance(points[i], points[j])
        if max_distance < d:
            max_distance = d

print(max_distance)

=======
Suggestion 2

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

n = int(input())
points = [list(map(int, input().split())) for i in range(n)]
max_dist = 0
for i in range(n):
    for j in range(i+1, n):
        max_dist = max(max_dist, dist(points[i][0], points[i][1], points[j][0], points[j][1]))
print(max_dist)

=======
Suggestion 3

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

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
Suggestion 4

def get_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

=======
Suggestion 5

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(0.5)

n=int(input())
points=[]
for i in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

distances=[]
for i in range(n):
    for j in range(i+1,n):
        distances.append(distance(points[i][0],points[i][1],points[j][0],points[j][1]))

print(max(distances))

=======
Suggestion 6

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int,input().split())))
    max_len = 0
    for i in range(N):
        for j in range(i+1,N):
            len = ((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)**0.5
            if len > max_len:
                max_len = len
    print(max_len)

=======
Suggestion 7

def main():
    import math
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    
    max_len = 0
    for i in range(N):
        for j in range(i+1, N):
            length = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
            if length > max_len:
                max_len = length
    print(max_len)

=======
Suggestion 8

def main():
    import sys
    import math
    import itertools
    import collections

    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans, math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2))

    print(ans)

=======
Suggestion 9

def getPoints(n):
    points = []
    for i in range(n):
        point = input().split()
        points.append((int(point[0]),int(point[1])))
    return points

=======
Suggestion 10

def main():
    # Get the number of points
    num_points = int(input())
    # Create a list of points
    points = []
    # Loop through the number of points
    for i in range(num_points):
        # Get the point
        point = input().split()
        # Add the point to the list
        points.append(point)
    # Create a list of distances
    distances = []
    # Loop through the points
    for i in range(num_points):
        # Loop through the points
        for j in range(num_points):
            # Get the distance between the points
            distance = (((int(points[i][0]) - int(points[j][0])) ** 2) + ((int(points[i][1]) - int(points[j][1])) ** 2)) ** 0.5
            # Add the distance to the list
            distances.append(distance)
    # Print the maximum distance
    print(max(distances))

main()
