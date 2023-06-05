Synthesizing 10/10 solutions

=======
Suggestion 1

def max_distance(x, y):
    max = 0
    for i in range(len(x)):
        for j in range(i + 1, len(y)):
            distance = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            if distance > max:
                max = distance
    return max

N = int(input())
x = []
y = []
for i in range(N):
    x_i, y_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)
print(max_distance(x, y))

=======
Suggestion 2

def max_len(x,y):
    max = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if (x[i]-x[j])**2+(y[i]-y[j])**2 > max:
                max = (x[i]-x[j])**2+(y[i]-y[j])**2
    return max**0.5

N = int(input())
x = []
y = []
for i in range(N):
    x1,y1 = map(int,input().split())
    x.append(x1)
    y.append(y1)
print(max_len(x,y))

=======
Suggestion 3

def get_max_distance(coordinates):
    max_distance = 0
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distance = ((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)**0.5
            if distance > max_distance:
                max_distance = distance
    return max_distance

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N = int(input())
    points = []
    for _ in range(N):
        point = input().split()
        point = [int(x) for x in point]
        points.append(point)
    max_dis = 0
    for i in range(N):
        for j in range(i+1, N):
            dis = ((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)**0.5
            if dis > max_dis:
                max_dis = dis
    print(max_dis)

=======
Suggestion 6

def get_max_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            if distance > max_distance:
                max_distance = distance
    return max_distance

=======
Suggestion 7

def get_max_dis(points):
    max_dis = 0
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            dis = ((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)**0.5
            if dis > max_dis:
                max_dis = dis
    return max_dis

=======
Suggestion 8

def get_max_length(points):
    max_length = 0
    for i in range(len(points) - 1):
        for j in range(i+1, len(points)):
            length = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            if length > max_length:
                max_length = length
    return max_length

=======
Suggestion 9

def main():
    import math
    N = int(input())
    list_x = []
    list_y = []
    for i in range(N):
        x,y = map(int,input().split())
        list_x.append(x)
        list_y.append(y)
    max_length = 0
    for i in range(N):
        for j in range(i+1,N):
            length = math.sqrt((list_x[i]-list_x[j])**2 + (list_y[i]-list_y[j])**2)
            if length > max_length:
                max_length = length
    print(max_length)

=======
Suggestion 10

def max_length():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    max = 0
    for i in range(n):
        for j in range(i+1,n):
            length = ((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
            if length > max:
                max = length
    print(max)
