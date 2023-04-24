Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    max_length = 0
    for i in range(N):
        for j in range(i + 1, N):
            length = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            if max_length < length:
                max_length = length
    print(max_length)

=======
Suggestion 2

def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, (X[i]-X[j])**2 + (Y[i]-Y[j])**2)
    print(ans**0.5)

=======
Suggestion 3

def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans = max(ans, (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
    print(ans ** 0.5)

=======
Suggestion 4

def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans = max(ans, (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)

    print(ans ** 0.5)

main()

=======
Suggestion 5

def main():
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, ((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) ** 0.5)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(list(map(int,input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans = max(ans,(p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)
    print(ans**0.5)

=======
Suggestion 8

def main():
    N = int(input())
    XY = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,((XY[i][0]-XY[j][0])**2+(XY[i][1]-XY[j][1])**2)**0.5)
    print(ans)

=======
Suggestion 9

def main():
    import sys
    import math

    #入力
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())

    #処理
    max = 0.0
    for i in range(N):
        for j in range(i+1, N):
            dist = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            if dist > max:
                max = dist

    #出力
    print(max)

=======
Suggestion 10

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x,y = map(int,input().split())
        points.append([x,y])
    #print(points)

    max_length = 0
    for i in range(n):
        for j in range(i+1,n):
            length = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
            max_length = max(max_length,length)
    print(max_length**0.5)
