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
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if x[i] == x[j]:
                ans += 1
                continue
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        x, y = map(int, input().split())
        X[i] = x
        Y[i] = y
    
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if -1 <= (Y[j]-Y[i])/(X[j]-X[i]) <= 1:
                ans += 1
    print(ans)

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
        for j in range(i+1, n):
            if y[j] - y[i] == 0:
                continue
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if -1 <= (y[j]-y[i])/(x[j]-x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    a = [list(map(int,input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if -1 <= (a[i][1]-a[j][1])/(a[i][0]-a[j][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (points[i][1]-points[j][1])/(points[i][0]-points[j][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) <= 1:
                count += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    points.sort()
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) <= 1:
                count += 1
    print(count)
