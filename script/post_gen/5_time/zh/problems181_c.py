Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (y[i]-y[j])*(x[i]-x[k]) == (x[i]-x[j])*(y[i]-y[k]):
                    print("Yes")
                    exit()

    print("No")

=======
Suggestion 2

def is_line(points):
    if len(points) < 3:
        return False
    else:
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    if points[i][0] == points[j][0] == points[k][0] or points[i][1] == points[j][1] == points[k][1]:
                        return True
        return False

=======
Suggestion 3

def is_same_line(p1,p2,p3):
    if p1[0] == p2[0] and p1[0] == p3[0]:
        return True
    if p1[0] == p2[0] or p1[0] == p3[0]:
        return False
    a1 = (p2[1]-p1[1])/(p2[0]-p1[0])
    a2 = (p3[1]-p1[1])/(p3[0]-p1[0])
    if a1 == a2:
        return True
    return False

=======
Suggestion 4

def get_slope(p1, p2):
    if p1[0] == p2[0]:
        return 'inf'
    elif p1[1] == p2[1]:
        return 0
    else:
        return (p1[1] - p2[1]) / (p1[0] - p2[0])

=======
Suggestion 5

def is_line(x1, y1, x2, y2, x3, y3):
    if x1 == x2 and x2 == x3:
        return True
    if x1 == x2 or x2 == x3:
        return False
    if (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2):
        return True
    return False

n = int(input())
points = []
for i in range(n):
    points.append(list(map(int,input().split())))

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if is_line(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                print('Yes')
                exit()
print('No')

=======
Suggestion 6

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (y[i]-y[j])*(x[i]-x[k]) == (y[i]-y[k])*(x[i]-x[j]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 7

def is_line(point1, point2, point3):
    #判断三点是否在一条直线上
    if (point1[0]-point2[0])*(point1[1]-point3[1]) == (point1[0]-point3[0])*(point1[1]-point2[1]):
        return True
    else:
        return False

=======
Suggestion 8

def solve():
    pass

=======
Suggestion 9

def is_line(points):
    if len(points) < 3:
        return False
    if points[0][0] == points[1][0] == points[2][0]:
        return True
    elif points[0][1] == points[1][1] == points[2][1]:
        return True
    elif points[0][0] == points[1][0] and points[1][0] == points[2][0]:
        return True
    elif points[0][1] == points[1][1] and points[1][1] == points[2][1]:
        return True
    elif points[0][0] == points[1][0] and points[1][0] == points[2][0]:
        return True
    elif points[0][1] == points[1][1] and points[1][1] == points[2][1]:
        return True
    else:
        k1 = (points[0][1] - points[1][1]) / (points[0][0] - points[1][0])
        k2 = (points[1][1] - points[2][1]) / (points[1][0] - points[2][0])
        if k1 == k2:
            return True
    return False

=======
Suggestion 10

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    #print(points)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                #print(points[i], points[j], points[k])
                if (points[j][1] - points[i][1]) * (points[k][0] - points[i][0]) == (points[k][1] - points[i][1]) * (points[j][0] - points[i][0]):
                    print("Yes")
                    return
    print("No")
