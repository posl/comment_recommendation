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
            if abs(y[j]-y[i]) <= abs(x[j]-x[i]):
                ans += 1
    print(ans)

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

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (y[j] - y[i]) / (x[j] - x[i]) <= 1:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    count = 0
    for i in range(n):
        for j in range(i):
            if abs(x[i] - x[j]) <= abs(y[i] - y[j]):
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (xy[i][1]-xy[j][1])/(xy[i][0]-xy[j][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    count = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if -1 <= (y2 - y1) / (x2 - x1) <= 1:
                count += 1

    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            slope = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
            if slope >= -1 and slope <= 1:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (xy[j][1] - xy[i][1])/(xy[j][0] - xy[i][0]) <= 1:
                count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    count = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(points[i][1]-points[j][1]) <= abs(points[i][0]-points[j][0]):
                count += 1
    print(count)
main()
# AC

=======
Suggestion 9

def check_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope >= -1 and slope <= 1

n = int(input())
points = []
for i in range(n):
    points.append(tuple(map(int, input().split())))

count = 0
for i in range(n):
    for j in range(i+1, n):
        if check_slope(points[i][0], points[i][1], points[j][0], points[j][1]):
            count += 1

print(count)

=======
Suggestion 10

def solve(n, points):
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                result += 1
    return result
