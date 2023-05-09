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
    X.sort()
    Y.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if (X[i] == X[j] and Y[k] == Y[l] and X[k] == X[l] and Y[i] == Y[j]) or (X[i] == X[k] and Y[j] == Y[l] and X[j] == X[l] and Y[i] == Y[k]) or (X[i] == X[l] and Y[j] == Y[k] and X[j] == X[k] and Y[i] == Y[l]):
                        ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if x[i] == x[j] and x[k] == x[l] and y[i] == y[k] and y[j] == y[l]:
                        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    xy.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if xy[i][0] < xy[j][0] and xy[i][1] < xy[j][1]:
                if [xy[i][0], xy[j][1]] in xy and [xy[j][0], xy[i][1]] in xy:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    xy = [list(map(int, input().split())) for i in range(N)]
    xy.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            if x1 < x2 and y1 < y2:
                if [x1, y2] in xy and [x2, y1] in xy:
                    ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0]:
                continue
            for k in range(j+1, N):
                if points[j][0] == points[k][0]:
                    continue
                if points[i][1] == points[k][1]:
                    continue
                for l in range(k+1, N):
                    if points[k][1] == points[l][1]:
                        continue
                    if points[l][0] == points[i][0] and points[l][1] == points[j][1]:
                        ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points = sorted(points)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in points and (x2, y1) in points:
                ans += 1
    print(ans//2)

=======
Suggestion 7

def solv():
    n = int(input())
    x_list = []
    y_list = []
    for i in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    x_list.sort()
    y_list.sort()
    x_dict = {}
    y_dict = {}
    for i in range(n):
        x_dict[x_list[i]] = i
        y_dict[y_list[i]] = i
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1 = x_list[i]
            x2 = x_list[j]
            y1 = y_list[i]
            y2 = y_list[j]
            if (x1, y2) in x_dict and (x2, y1) in x_dict:
                ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    points = list(map(list, zip(*points)))
    points[0] = [points[0][0]] + [0] + points[0]
    points[1] = [0] + [points[1][0]] + points[1

=======
Suggestion 9

def main():
    N = int(input())
    points = []
    for _ in range(N):
        points.append([int(x) for x in input().split()])
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if points[i][0] < points[j][0] and points[i][1] < points[j][1]:
                if [points[i][0], points[j][1]] in points and [points[j][0], points[i][1]] in points:
                    ans += 1
    print(ans)

=======
Suggestion 10

def get_input():
    n = int(input())
    points = []
    for i in range(n):
        points.append([int(x) for x in input().split()])
    return n, points
