Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                x3, y3 = xy[k]

                if (x1-x2)*(y2-y3) == (x2-x3)*(y1-y2):
                    print("Yes")
                    return

    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1, y1 = XY[i]
                x2, y2 = XY[j]
                x3, y3 = XY[k]

                if (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 3

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1, y1 = XY[i]
                x2, y2 = XY[j]
                x3, y3 = XY[k]
                # 3点が同一直線上にあるかどうかの判定
                if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 4

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (XY[j][0] - XY[i][0]) * (XY[k][1] - XY[i][1]) == (XY[j][1] - XY[i][1]) * (XY[k][0] - XY[i][0]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 5

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (XY[j][1] - XY[i][1]) * (XY[k][0] - XY[j][0]) == (XY[k][1] - XY[j][1]) * (XY[j][0] - XY[i][0]):
                    print("Yes")
                    return
    print("No")

=======
Suggestion 6

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (points[j][1] - points[i][1]) * (points[k][0] - points[j][0]) == (points[k][1] - points[j][1]) * (points[j][0] - points[i][0]):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 7

def main():
    N = int(input())
    P = []
    for _ in range(N):
        x,y = map(int,input().split())
        P.append([x,y])
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                x1,y1 = P[i]
                x2,y2 = P[j]
                x3,y3 = P[k]
                if (x2-x1)*(y3-y1) == (x3-x1)*(y2-y1):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 8

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    ans = 'No'
    for i in range(N):
        for j in range(N):
            if i == j: continue
            for k in range(N):
                if k == j or k == i: continue
                if (y[j]-y[i])*(x[k]-x[i]) == (y[k]-y[i])*(x[j]-x[i]):
                    ans = 'Yes'
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    if N < 3:
        print("No")
        return
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (Y[j] - Y[i]) * (X[k] - X[j]) == (X[j] - X[i]) * (Y[k] - Y[j]):
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 10

def main():
    N = int(input())
    xy = []
    for i in range(N):
        xy.append(list(map(int, input().split())))

    #print(xy)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                #print(xy[i], xy[j], xy[k])
                if (xy[j][1] - xy[i][1])*(xy[k][0] - xy[j][0]) == (xy[j][0] - xy[i][0])*(xy[k][1] - xy[j][1]):
                    print("Yes")
                    return
    print("No")
    return
