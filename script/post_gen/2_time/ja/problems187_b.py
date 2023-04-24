Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (y[j]-y[i])/(x[j]-x[i]) <= 1:
                cnt += 1
    print(cnt)

=======
Suggestion 4

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
            if (y[i] - y[j]) / (x[i] - x[j]) >= -1 and (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1

    print(ans)

main()

=======
Suggestion 5

def main():
    n = int(input())
    xy = []
    for i in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (xy[j][1]-xy[i][1])/(xy[j][0]-xy[i][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (y[j] - y[i]) / (x[j] - x[i]) <= 1 and (y[j] - y[i]) / (x[j] - x[i]) >= -1:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append([x, y])
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    data = [list(map(int, input().split())) for i in range(n)]
    data.sort()
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (data[j][1] - data[i][1]) / (data[j][0] - data[i][0]) <= 1:
                cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    N = int(input())
    #print(N)
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    #print(x)
    #print(y)
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (y[i] - y[j]) / (x[i] - x[j]) >= -1 and (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                count += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    point = [list(map(int, input().split())) for _ in range(n)]
    point.sort()
    slope = []
    for i in range(n-1):
        for j in range(i+1, n):
            #print(point[i][0], point[i][1], point[j][0], point[j][1])
            if point[i][0] != point[j][0]:
                slope.append((point[j][1]-point[i][1])/(point[j][0]-point[i][0]))
    slope.sort()
    ans = 0
    for i in range(len(slope)-1):
        if slope[i] >= -1 and slope[i] <= 1:
            ans += 1
    print(ans)
