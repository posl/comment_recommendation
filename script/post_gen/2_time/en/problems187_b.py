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
        for j in range(i+1, N):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (y[j]-y[i])/(x[j]-x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (y[j]-y[i])/(x[j]-x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j]:
                continue
            if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if points[i][1] - points[j][1] != 0:
                if -1 <= (points[i][0] - points[j][0]) / (points[i][1] - points[j][1]) <= 1:
                    count += 1
    print(count)

=======
Suggestion 6

def main():
    #input
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    #compute
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if -1 <= (Y[j]-Y[i])/(X[j]-X[i]) <= 1:
                ans += 1

    #output
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    slopes = []
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0]:
                slopes.append(10000000000)
            else:
                slopes.append((points[i][1] - points[j][1]) / (points[i][0] - points[j][0]))
    slopes = sorted(slopes)
    print(slopes)
    ans = 0
    for i in range(len(slopes)):
        for j in range(i+1, len(slopes)):
            if slopes[i] < slopes[j] and slopes[j] <= 1:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    p = [tuple(map(int, input().split())) for _ in range(N)]
    p.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (p[i][1] - p[j][1]) / (p[i][0] - p[j][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    slopes = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0]:
                slopes[i] += 1
                slopes[j] += 1
            else:
                slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                if -1 <= slope <= 1:
                    slopes[i] += 1
                    slopes[j] += 1
    print(sum([s * (s-1) // 2 for s in slopes]))

=======
Suggestion 10

def main():
    # Your code here
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if -1 <= (y[j]-y[i])/(x[j]-x[i]) <= 1:
                ans += 1
    print(ans)
