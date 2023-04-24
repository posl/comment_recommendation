Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if (X[i] - X[j]) * (Y[i] - Y[k]) == (X[i] - X[k]) * (Y[i] - Y[j]):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 2

def main():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if (P[i][1] - P[j][1]) * (P[j][0] - P[k][0]) == (P[j][1] - P[k][1]) * (P[i][0] - P[j][0]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 3

def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (points[i][0] - points[j][0]) * (points[i][1] - points[k][1]) == (points[i][0] - points[k][0]) * (points[i][1] - points[j][1]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 4

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                a = (x2 - x1) * (y3 - y1)
                b = (x3 - x1) * (y2 - y1)
                if a == b:
                    print('Yes')
                    return
    print('No')

main()

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 6

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1, y1 = XY[i]
                x2, y2 = XY[j]
                x3, y3 = XY[k]
                if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
                    print("Yes")
                    return

    print("No")

=======
Suggestion 7

def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append((x, y))
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if is_on_same_line(XY[i], XY[j], XY[k]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 8

def main():
    N = int(input())
    x, y = [], []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (x[i]-x[j])*(y[j]-y[k]) == (x[j]-x[k])*(y[i]-y[j]):
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 10

def main():
    #input
    n = int(input())
    xys = [tuple(map(int, input().split())) for _ in range(n)]

    #compute
    ans = 'No'
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (xys[i][0]-xys[j][0])*(xys[i][1]-xys[k][1]) == (xys[i][0]-xys[k][0])*(xys[i][1]-xys[j][1]):
                    ans = 'Yes'
                    break

    #output
    print(ans)
