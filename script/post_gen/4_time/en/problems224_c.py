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
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if (X[j]-X[i])*(Y[k]-Y[i]) != (X[k]-X[i])*(Y[j]-Y[i]):
                    ans += 1
    print(ans)

=======
Suggestion 2

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
            for k in range(j+1, N):
                a = X[j]-X[i]
                b = Y[j]-Y[i]
                c = X[k]-X[i]
                d = Y[k]-Y[i]
                if a*d != b*c:
                    ans += 1
    print(ans)

=======
Suggestion 3

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
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (Y[j] - Y[i]) * (X[k] - X[i]) - (Y[k] - Y[i]) * (X[j] - X[i]) != 0:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (X[j]-X[i])*(Y[k]-Y[i]) - (Y[j]-Y[i])*(X[k]-X[i]) != 0:
                    cnt += 1
    print(cnt)

=======
Suggestion 5

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
            for k in range(j+1, n):
                if (x[j]-x[i])*(y[k]-y[i]) != (x[k]-x[i])*(y[j]-y[i]):
                    count += 1
    print(count)

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
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                ans += is_triangle(x[i], y[i], x[j], y[j], x[k], y[k])
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (x[j] - x[i]) * (y[k] - y[i]) - (y[j] - y[i]) * (x[k] - x[i]) != 0:
                    ans += 1
    print(ans)

=======
Suggestion 8

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
            for k in range(j + 1, n):
                if (y[i] - y[j]) * (x[i] - x[k]) != (y[i] - y[k]) * (x[i] - x[j]):
                    ans += 1
    print(ans)

=======
Suggestion 9

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
            for k in range(j+1, n):
                if x[i] == x[j] and x[j] == x[k]:
                    continue
                if x[i] == x[j]:
                    if (y[j]-y[i])*(x[k]-x[i]) == (y[k]-y[i])*(x[j]-x[i]):
                        continue
                elif x[j] == x[k]:
                    if (y[j]-y[i])*(x[k]-x[i]) == (y[k]-y[i])*(x[j]-x[i]):
                        continue
                elif x[i] == x[k]:
                    if (y[j]-y[i])*(x[k]-x[i]) == (y[k]-y[i])*(x[j]-x[i]):
                        continue
                if (y[j]-y[i])*(x[k]-x[i]) == (y[k]-y[i])*(x[j]-x[i]):
                    continue
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    #print(N)
    points = []
    for i in range(N):
        x,y = map(int,input().split())
        points.append((x,y))

    #print(points)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if isTriangle(points[i],points[j],points[k]):
                    count += 1
    print(count)
