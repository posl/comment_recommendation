Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max = 0
    for i in range(n):
        for j in range(i+1, n):
            distance = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            if distance > max:
                max = distance
    print(max)

=======
Suggestion 2

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max_length = 0
    for i in range(n):
        for j in range(i+1, n):
            length = ((x[i] - x[j])**2 + (y[i] - y[j])**2)**(1/2)
            if length > max_length:
                max_length = length
    print(max_length)

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)

    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans, (x[i]-x[j])**2 + (y[i]-y[j])**2)

    print(ans**0.5)

=======
Suggestion 4

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            ans = max(ans,(x[i]-x[j])**2+(y[i]-y[j])**2)
    print(ans**0.5)

=======
Suggestion 5

def main():
    n = int(input())
    points = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans, (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
    print(ans**0.5)

main()

=======
Suggestion 7

def main():
    import math
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, math.sqrt((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2))
    print(ans)
    return

main()

=======
Suggestion 8

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    max = 0
    for i in range(n-1):
        for j in range(i+1, n):
            dist = ((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
            if dist > max:
                max = dist
    print(max)

=======
Suggestion 9

def main():
    import sys
    from itertools import combinations
    import math
    N = int(sys.stdin.readline())
    points = []
    for i in range(N):
        x,y = map(int,sys.stdin.readline().split())
        points.append((x,y))
    max_len = 0
    for comb in combinations(points,2):
        x1,y1 = comb[0]
        x2,y2 = comb[1]
        len = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        if len > max_len:
            max_len = len
    print(max_len)

main()

=======
Suggestion 10

def main():
    import sys
    import math
    N = int(sys.stdin.readline())
    xys = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    max_dist = -1
    for i in range(N):
        for j in range(i + 1, N):
            dist = math.sqrt((xys[i][0] - xys[j][0]) ** 2 + (xys[i][1] - xys[j][1]) ** 2)
            if dist > max_dist:
                max_dist = dist
    print(max_dist)
