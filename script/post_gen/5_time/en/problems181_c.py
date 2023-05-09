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
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (x[i] - x[j]) * (y[i] - y[k]) == (x[i] - x[k]) * (y[i] - y[j]):
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (points[i][0]-points[j][0])*(points[i][1]-points[k][1]) == (points[i][0]-points[k][0])*(points[i][1]-points[j][1]):
                    print("Yes")
                    exit()
    print("No")

=======
Suggestion 3

def check(a,b,c):
    if (a[0] == b[0] and a[0] == c[0]) or (a[1] == b[1] and a[1] == c[1]):
        return True
    if (a[1] - b[1]) * (a[0] - c[0]) == (a[0] - b[0]) * (a[1] - c[1]):
        return True
    else:
        return False

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if check(p[i],p[j],p[k]):
                print("Yes")
                exit()
print("No")

=======
Suggestion 4

def is_on_line(x1, y1, x2, y2, x3, y3):
    return (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2)

n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if is_on_line(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]):
                print('Yes')
                exit()
print('No')

=======
Suggestion 5

def check_points(points):
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if (points[i][0] - points[j][0]) * (points[i][1] - points[k][1]) == (points[i][0] - points[k][0]) * (points[i][1] - points[j][1]):
                    return True
    return False

=======
Suggestion 6

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    # print(points)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # print(i, j, k)
                if (points[j][1]-points[i][1])*(points[k][0]-points[i][0]) == (points[k][1]-points[i][1])*(points[j][0]-points[i][0]):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 7

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = input().split()
        points.append((int(x), int(y)))
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (points[i][0] - points[j][0]) * (points[i][1] - points[k][1]) == (points[i][0] - points[k][0]) * (points[i][1] - points[j][1]):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 8

def is_on_the_same_line(x1,y1,x2,y2,x3,y3):
    if x1 == x2 == x3:
        return True
    elif x1 == x2 or x2 == x3:
        return False
    else:
        return (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2)

n = int(input())
points = []
for i in range(n):
    point = input().split()
    points.append([int(point[0]),int(point[1])])
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if is_on_the_same_line(points[i][0],points[i][1],points[j][0],points[j][1],points[k][0],points[k][1]):
                print("Yes")
                exit()
print("No")

=======
Suggestion 9

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(tuple(map(int, input().split())))
    
    points.sort()
    
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if ((points[i][0] - points[j][0]) * (points[j][1] - points[k][1]) == (points[i][1] - points[j][1]) * (points[j][0] - points[k][0])):
                    print("Yes")
                    return
    
    print("No")
    return

=======
Suggestion 10

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    #print(points)
    if N == 3:
        print("Yes")
        return
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                #print(points[i], points[j], points[k])
                if (points[j][0] - points[i][0]) * (points[k][1] - points[i][1]) == (points[k][0] - points[i][0]) * (points[j][1] - points[i][1]):
                    print("Yes")
                    return
    print("No")
    return
