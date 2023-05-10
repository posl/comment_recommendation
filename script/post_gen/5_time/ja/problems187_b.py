Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
            if -1 <= slope and slope <= 1:
                cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if xy[i][1] - xy[j][1] <= xy[i][0] - xy[j][0] <= xy[i][1] - xy[j][1]:
                ans += 1
            elif xy[i][1] - xy[j][1] >= xy[i][0] - xy[j][0] >= xy[i][1] - xy[j][1]:
                ans += 1
    print(ans)

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
        for j in range(i+1, n):
            if -1 <= (y[i]-y[j])/(x[i]-x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if -1 <= (points[j][1] - points[i][1])/(points[j][0] - points[i][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    #n = int(input())
    #a = list(map(int, input().split()))
    #n, m = map(int, input().split())
    #a = [list(map(int, input().split())) for _ in range(n)]
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(y[i]-y[j]) <= abs(x[i]-x[j]):
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if -1 <= (y[i] - y[j])/(x[i] - x[j]) <= 1:
                count += 1
    print(count)
