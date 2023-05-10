Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)

    xy = list(zip(x, y))
    xy.sort()
    x.sort()
    y.sort()

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if x[i] < x[j] and y[i] < y[j]:
                if (x[i], y[j]) in xy and (x[j], y[i]) in xy:
                    ans += 1

    print(ans)

=======
Suggestion 2

def get_input():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return n, points

=======
Suggestion 3

def main():
    n = int(input())
    points = [list(map(int,input().split())) for _ in range(n)]
    points.sort()
    points = list(map(list,zip(*points)))
    x = points[0]
    y = points[1]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j]:
                for k in range(j+1,n):
                    if x[i] == x[k]:
                        if y[i] == y[j] and y[k] == y[i]:
                            ans += 1
                    else:
                        break
            else:
                break
    print(ans)

=======
Suggestion 4

def get_input():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    return n, x, y

=======
Suggestion 5

def solve():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] != points[j][0] and points[i][1] != points[j][1]:
                if [points[i][0], points[j][1]] in points and [points[j][0], points[i][1]] in points:
                    ans += 1
    print(ans//2)

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if x[i] == x[j] and y[k] == y[l] and x[k] == x[l] and y[i] == y[j]:
                        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    points = []
    for _ in range(N):
        points.append(list(map(int, input().split())))

    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2 or y1 == y2:
                continue
            if [x1, y2] in points and [x2, y1] in points:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    xy = []
    for i in range(N):
        x,y = map(int, input().split())
        xy.append([x,y])
    xy.sort()
    answer = 0
    for i in range(N):
        for j in range(i+1,N):
            if xy[i][0] == xy[j][0]:
                for k in range(j+1,N):
                    if xy[j][0] == xy[k][0]:
                        for l in range(k+1,N):
                            if xy[k][0] == xy[l][0]:
                                answer += 1
            else:
                break
    print(answer)

=======
Suggestion 9

def main():
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if x[i] == x[j] and x[k] == x[l] and y[i] == y[k] and y[j] == y[l]:
                        ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, input().split())))
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
    print(ans//2)
