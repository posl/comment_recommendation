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
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                ans += 1
    print(ans)
    return 0

=======
Suggestion 3

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
        for j in range(i+1, N):
            if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (Y[j] - Y[i]) / (X[j] - X[i]) <= 1:
                cnt += 1

    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    x_y = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (x_y[i][1] - x_y[j][1]) / (x_y[i][0] - x_y[j][0]) <= 1:
                cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    point_list = []
    for i in range(N):
        x, y = map(int, input().split())
        point_list.append((x, y))

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if point_list[i][0] == point_list[j][0]:
                continue
            if -1 <= (point_list[i][1] - point_list[j][1]) / (point_list[i][0] - point_list[j][0]) <= 1:
                ans += 1

    print(ans)

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 9

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    points.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] == points[j][0]:
                continue
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                count += 1
    print(count)

=======
Suggestion 10

def solve():
    n = int(input())
    xy = []
    for _ in range(n):
        xy.append(list(map(int, input().split())))
    xy.sort()
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if xy[i][0] == xy[j][0]:
                continue
            elif xy[i][1] <= xy[j][1] and xy[i][0] <= xy[j][0]:
                if (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) <= 1:
                    ans += 1
            elif xy[i][1] >= xy[j][1] and xy[i][0] >= xy[j][0]:
                if (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) >= 1:
                    ans += 1
            elif xy[i][1] >= xy[j][1] and xy[i][0] <= xy[j][0]:
                if (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) >= -1:
                    ans += 1
            elif xy[i][1] <= xy[j][1] and xy[i][0] >= xy[j][0]:
                if (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) <= -1:
                    ans += 1
    print(ans)
