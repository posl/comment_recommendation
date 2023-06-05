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
        for j in range(n):
            if x[i] < x[j] and y[i] < y[j]:
                if x[i] in x and y[j] in y:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] < points[j][0] and points[i][1] < points[j][1]:
                if (points[i][0], points[j][1]) in points and (points[j][0], points[i][1]) in points:
                    count += 1
    print(count)

=======
Suggestion 3

def solve():
    pass

=======
Suggestion 4

def solve():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = [int(_) for _ in input().split()]
        x.append(x_i)
        y.append(y_i)
    x.sort()
    y.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if x[i] < x[j] and y[i] < y[j]:
                if x[i] in x and x[j] in x and y[i] in y and y[j] in y:
                    ans += 1
    print(ans)

=======
Suggestion 5

def getXY():
    x = input("请输入x坐标：")
    y = input("请输入y坐标：")
    return x,y

=======
Suggestion 6

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
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if dx == 0 or dy == 0:
                continue
            if x[i] - dy in x and y[i] + dx in y:
                if x[j] - dy in x and y[j] + dx in y:
                    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(raw_input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, raw_input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            if (x[i], y[j]) in zip(x, y) and (x[j], y[i]) in zip(x, y):
                ans += 1
    print ans

=======
Suggestion 8

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x0, y0 = map(int, input().split())
        x.append(x0)
        y.append(y0)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if x[i] != x[j] and y[i] != y[j]:
                if x[i] in x and y[j] in y:
                    count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(raw_input())
    points = []
    for i in range(n):
        x, y = map(int, raw_input().split())
        points.append((x, y))
    points.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in points and (x2, y1) in points:
                ans += 1
    print ans / 2

=======
Suggestion 10

def solve(n, points):
    x = {}
    y = {}
    for p in points:
        if p[0] not in x:
            x[p[0]] = 1
        else:
            x[p[0]] += 1
        if p[1] not in y:
            y[p[1]] = 1
        else:
            y[p[1]] += 1
    ans = 0
    for p in points:
        ans += (x[p[0]] - 1) * (y[p[1]] - 1)
    return ans
