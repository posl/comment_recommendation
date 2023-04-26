Synthesizing 10/10 solutions

=======
Suggestion 1

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
            ans = max(ans, (x[i] - x[j])**2 + (y[i] - y[j])**2)
    print(ans**0.5)

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
        for j in range(i + 1, N):
            ans = max(ans, (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
    print(ans ** 0.5)

=======
Suggestion 3

def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, (xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2)
    print(ans**0.5)

main()

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
            ans = max(ans, (x[i]-x[j])**2 + (y[i]-y[j])**2)

    print(ans**0.5)

=======
Suggestion 5

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
        for j in range(i+1,N):
            ans = max(ans, ((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5)
    print(ans)

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
            ans = max(ans, (x[i]-x[j])**2+(y[i]-y[j])**2)
    print(ans**0.5)

=======
Suggestion 7

def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    max_length = 0
    for i in range(N):
        for j in range(i + 1, N):
            length = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
            max_length = max(max_length, length)
    print(max_length)

=======
Suggestion 8

def main():
    N = int(input())
    xy = [[int(i) for i in input().split()] for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**0.5)
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    #print(x)
    #print(y)
    max_length = 0
    for i in range(n):
        for j in range(i+1, n):
            length = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**(1/2)
            if max_length < length:
                max_length = length
    print(max_length)

=======
Suggestion 10

def main():
    N = int(input())
    xy = []
    for i in range(N):
        x, y = map(int, input().split())
        xy.append((x, y))
    max_dist = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = ((xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2)**0.5
            if dist > max_dist:
                max_dist = dist
    print(max_dist)
