Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    max_length = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            length = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            if length > max_length:
                max_length = length

    print(max_length)

=======
Suggestion 2

def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

n=int(input())
points=[]
for i in range(n):
    x,y=map(int,input().split())
    points.append((x,y))

max_distance=0
for i in range(n):
    for j in range(i+1,n):
        distance=get_distance(points[i][0],points[i][1],points[j][0],points[j][1])
        if distance>max_distance:
            max_distance=distance

print(max_distance)

=======
Suggestion 3

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))

    max_len = 0.0
    for i in range(n):
        for j in range(i+1, n):
            x = points[i][0] - points[j][0]
            y = points[i][1] - points[j][1]
            length = (x**2 + y**2)**0.5
            if length > max_len:
                max_len = length

    print(max_len)

=======
Suggestion 4

def main():
    #入力
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append([x, y])

    #処理
    max_dist = 0
    for i in range(N-1):
        for j in range(i+1, N):
            dist = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
            if dist > max_dist:
                max_dist = dist

    #出力
    print(max_dist**0.5)

=======
Suggestion 5

def get_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


N = int(input())
point_list = []
for i in range(N):
    point_list.append(list(map(int, input().split())))

max_distance = 0
for i in range(N):
    for j in range(i+1, N):
        distance = get_distance(point_list[i][0], point_list[i][1], point_list[j][0], point_list[j][1])
        if distance > max_distance:
            max_distance = distance

print(max_distance)

=======
Suggestion 6

def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

=======
Suggestion 7

def main():
    import sys
    import math
    n = int(sys.stdin.readline().strip())
    points = []
    for i in range(n):
        x,y = map(int,sys.stdin.readline().strip().split())
        points.append([x,y])
    max_distance = 0
    for i in range(n):
        for j in range(i+1,n):
            distance = math.sqrt((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
            if distance > max_distance:
                max_distance = distance
    print(max_distance)

=======
Suggestion 8

def main():
    N = int(input())
    points = []
    max_len = 0
    for _ in range(N):
        points.append(tuple(map(int, input().split())))
    for i in range(N):
        for j in range(i+1, N):
            len = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
            if len > max_len:
                max_len = len
    print(max_len**0.5)

=======
Suggestion 9

def get_max_distance(points):
    max_distance = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = get_distance(points[i], points[j])
            if distance > max_distance:
                max_distance = distance
    return max_distance

=======
Suggestion 10

def main():
    import sys
    import math

    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)

    max_len = 0
    for i in range(N-1):
        for j in range(i+1, N):
            len_i_j = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if len_i_j > max_len:
                max_len = len_i_j
    print(max_len)
