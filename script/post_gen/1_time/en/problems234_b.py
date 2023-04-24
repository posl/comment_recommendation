Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    max_length = 0
    for i in range(N):
        for j in range(i + 1, N):
            length = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            if length > max_length:
                max_length = length
    print(max_length)

=======
Suggestion 2

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
        for j in range(i + 1, n):
            ans = max(ans, (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
    print(ans ** 0.5)

=======
Suggestion 3

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    max_dist = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                dist = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5
                if dist > max_dist:
                    max_dist = dist
    print(max_dist)

=======
Suggestion 4

def main():
    import math
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    p = []
    for _ in range(N):
        p.append(tuple(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, ((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2)**0.5)
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    y = []
    for i in range(0,n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(0,n):
        for j in range(i,n):
            ans = max(ans,((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5)
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        tmp = input().split()
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans, (x[i]-x[j])**2 + (y[i]-y[j])**2)
    print(ans**0.5)

=======
Suggestion 8

def main():
    N = int(input())
    points = [[int(x) for x in input().split()] for _ in range(N)]
    max_length = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                length = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
                if length > max_length:
                    max_length = length
    print(max_length)

=======
Suggestion 9

def main():
    import sys
    import math
    #入力
    readline = sys.stdin.readline
    N = int(readline())
    points = []
    for i in range(N):
        x,y = map(int,readline().split())
        points.append((x,y))
    # 2点間の距離を求める
    def distance(p1,p2):
        return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    # 距離を全探索
    max_distance = 0
    for i in range(N-1):
        for j in range(i+1,N):
            max_distance = max(max_distance,distance(points[i],points[j]))
    # 出力
    print(max_distance)

=======
Suggestion 10

def main():
    import math
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int,input().split())))
    #print(points)
    max_distance = 0
    for i in range(N):
        for j in range(i+1,N):
            distance = math.sqrt((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
            if distance > max_distance:
                max_distance = distance
    print(max_distance)
