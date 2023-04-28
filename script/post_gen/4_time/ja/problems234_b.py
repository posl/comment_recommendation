Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            ans = max(ans, ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
    print(ans)

=======
Suggestion 2

def main():
    import math
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max = 0
    for i in range(N):
        for j in range(i+1,N):
            tmp = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if tmp > max:
                max = tmp
    print(max)
    return 0

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    max = 0
    for i in range(n):
        for j in range(i+1,n):
            tmp = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**(1/2)
            if max < tmp:
                max = tmp
    print(max)

=======
Suggestion 4

def main():
    import math
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_len = max(max_len, math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2))
    print(max_len)
main()

=======
Suggestion 5

def get_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        ans = max(ans, get_distance(x1, y1, x2, y2))

print(ans)

=======
Suggestion 6

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

n = int(input())
l = []
for i in range(n):
    x,y = map(int,input().split())
    l.append((x,y))

ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans = max(ans,dist(l[i][0],l[i][1],l[j][0],l[j][1]))

print(ans)

=======
Suggestion 7

def main():
    import sys
    import math
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
            ans = max(ans, math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2))
    print(ans)

=======
Suggestion 8

def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

n = int(input())
x = []
y = []
for _ in range(n):
    x1,y1 = map(int,input().split())
    x.append(x1)
    y.append(y1)

ans = 0
for i in range(n):
    for j in range(i+1,n):
        d = get_distance(x[i],y[i],x[j],y[j])
        if d > ans:
            ans = d

print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    #print(points)
    max_len = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            #print(x1, y1, x2, y2)
            len = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            if max_len < len:
                max_len = len
    print(max_len)

=======
Suggestion 10

def get_input():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    return n, points
