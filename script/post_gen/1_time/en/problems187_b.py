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
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (y[i] - y[j]) / (x[i] - x[j]) <= 1 and (y[i] - y[j]) / (x[i] - x[j]) >= -1:
                count += 1
    print(count)

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
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (data[j][1] - data[i][1]) / (data[j][0] - data[i][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    x, y = [], []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    p.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (p[j][1] - p[i][1]) / (p[j][0] - p[i][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (Y[j]-Y[i])/(X[j]-X[i]) <= 1:
                count += 1

    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    points = []
    for i in range(N):
        x,y = map(int,input().split())
        points.append((x,y))
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            x1,y1 = points[i]
            x2,y2 = points[j]
            if x1 == x2:
                continue
            slope = (y1 - y2)/(x1 - x2)
            if slope >= -1 and slope <= 1:
                count += 1
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    slopes = [0] * N
    for i in range(N):
        for j in range(N):
            if i < j:
                if points[i][0] != points[j][0]:
                    slopes[i] += 1
                    slopes[j] += 1
    ans = 0
    for s in slopes:
        ans += s
    print(ans // 2)
