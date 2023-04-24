Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = [0 for i in range(N)]
    y = [0 for i in range(N)]
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if -1 <= (y[j]-y[i])/(x[j]-x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 2

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
            if -1 <= (y[j]-y[i])/(x[j]-x[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (Y[j] - Y[i]) / (X[j] - X[i]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if y[i] - y[j] >= x[i] - x[j] and y[i] - y[j] <= x[i] - x[j]:
                count += 1
    print(count)
main()

=======
Suggestion 6

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
        for j in range(i+1, N):
            if (-1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1):
                ans += 1
    print(ans)

=======
Suggestion 7

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
        for j in range(i+1, N):
            if (y[j] - y[i]) / (x[j] - x[i]) <= 1 and (y[j] - y[i]) / (x[j] - x[i]) >= -1:
                count += 1
    print(count)

=======
Suggestion 8

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
Suggestion 9

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (y[i] - y[j]) / (x[i] - x[j]) <= 1:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    xy = []
    for i in range(n):
        x, y = map(int, input().split())
        xy.append((x, y))
    xy.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if -1 <= (xy[j][1] - xy[i][1]) / (xy[j][0] - xy[i][0]) <= 1:
                ans += 1
    print(ans)
