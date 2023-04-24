Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, ((X[i]-X[j])**2+(Y[i]-Y[j])**2)**0.5)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    max = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                l = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5
                if l > max:
                    max = l
    print(max)

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, ((x[i] - x[j])**2 + (y[i] - y[j])**2)**0.5)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    max_dist = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
            if dist > max_dist:
                max_dist = dist
    print(max_dist)

=======
Suggestion 5

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]

    max_length = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            length = ((x1-x2)**2 + (y1-y2)**2)**0.5
            max_length = max(max_length, length)
    print(max_length)

=======
Suggestion 6

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    max_length = 0
    for i in range(N):
        for j in range(i + 1, N):
            length = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
            if length > max_length:
                max_length = length
    print(max_length)

=======
Suggestion 7

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_len = max(max_len, (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
    print(max_len ** 0.5)

=======
Suggestion 8

def main():
    #input
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i],Y[i] = map(int,input().split())

    #compute
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,(X[i]-X[j])**2+(Y[i]-Y[j])**2)

    #output
    print(ans**0.5)

=======
Suggestion 9

def main():
    import sys
    import math
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    max = 0
    for i in range(n-1):
        for j in range(i+1,n):
            tmp = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            if tmp > max:
                max = tmp
    print(max)

=======
Suggestion 10

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    max = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                length = ((A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2) ** 0.5
                if length > max:
                    max = length

    print(max)
