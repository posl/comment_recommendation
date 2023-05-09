Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
            if slope >= -1 and slope <= 1:
                count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if -1 <= (y2 - y1) / (x2 - x1) <= 1:
                count += 1
    print(count)

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
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) <= 1:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(points[j][1] - points[i][1]) <= abs(points[j][0] - points[i][0]):
                count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(points[i][0] - points[j][0]) <= abs(points[i][1] - points[j][1]):
                ans += 1

    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) <= 1:
                count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    x, y = [0] * n, [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 9

def solve():
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (xy[i][1] - xy[j][1]) / (xy[i][0] - xy[j][0]) <= 1:
                ans += 1

    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append([int(x) for x in input().split()])

    result = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                result += 1

    print(result)
