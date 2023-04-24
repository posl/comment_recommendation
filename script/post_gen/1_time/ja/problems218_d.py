Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = [0]*N
    y = [0]*N
    for i in range(N):
        x[i],y[i] = map(int,input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (x[j]-x[i])*(y[k]-y[i]) == (y[j]-y[i])*(x[k]-x[i]):
                    continue
                for l in range(k+1,N):
                    if (x[k]-x[j])*(y[l]-y[j]) == (y[k]-y[j])*(x[l]-x[j]):
                        continue
                    if (x[l]-x[k])*(y[i]-y[k]) == (y[l]-y[k])*(x[i]-x[k]):
                        continue
                    if (x[i]-x[l])*(y[j]-y[l]) == (y[i]-y[l])*(x[j]-x[l]):
                        continue
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append([x, y])
    ans = 0
    for i in range(N):
        for j in range(N):
            if XY[i][0] == XY[j][0] or XY[i][1] == XY[j][1]:
                continue
            for k in range(N):
                if XY[i][0] == XY[k][0] or XY[i][1] == XY[k][1]:
                    continue
                if XY[j][0] == XY[k][0] or XY[j][1] == XY[k][1]:
                    continue
                if XY[i][0] == XY[j][0] and XY[j][0] == XY[k][0]:
                    ans += 1
                elif XY[i][1] == XY[j][1] and XY[j][1] == XY[k][1]:
                    ans += 1
    print(ans//2)

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
    X = list(set(X))
    Y = list(set(Y))
    X.sort()
    Y.sort()
    ans = 0
    for i in range(len(X)):
        for j in range(i+1, len(X)):
            for k in range(len(Y)):
                for l in range(k+1, len(Y)):
                    cnt = 0
                    for m in range(N):
                        if X[i] <= X[m] <= X[j] and Y[k] <= Y[m] <= Y[l]:
                            cnt += 1
                    if cnt == 4:
                        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    #入力
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    #処理
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                for l in range(k+1,N):
                    if x[i] == x[j] and y[j] == y[k] and x[k] == x[l] and y[l] == y[i]:
                        ans += 1
    #出力
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    P = []
    for i in range(N):
        x,y = map(int,input().split())
        P.append((x,y))
    P.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            x1,y1 = P[i]
            x2,y2 = P[j]
            if x1==x2 or y1==y2:
                continue
            if (x1,y2) in P and (x2,y1) in P:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if (x1, y2) in points and (x2, y1) in points:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    x_y = []
    for i in range(N):
        x_y.append(list(map(int,input().split())))
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if x_y[i][0] == x_y[j][0] and x_y[i][1] == x_y[k][1] and x_y[j][1] == x_y[k][0]:
                    count += 1
                elif x_y[i][0] == x_y[k][0] and x_y[i][1] == x_y[j][1] and x_y[k][1] == x_y[j][0]:
                    count += 1
                elif x_y[j][0] == x_y[k][0] and x_y[j][1] == x_y[i][1] and x_y[k][1] == x_y[i][0]:
                    count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int,input().split())))
    points.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if points[i][0] == points[j][0] and points[j][0] != points[k][0] and points[j][1] != points[k][1]:
                    if points[i][1] < points[j][1] < points[k][1]:
                        ans += 1
                    elif points[i][1] > points[j][1] > points[k][1]:
                        ans += 1
                    elif points[i][1] == points[j][1] and points[j][1] == points[k][1]:
                        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    points = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for k in range(N):
                if i == k or j == k:
                    continue
                for l in range(N):
                    if i == l or j == l or k == l:
                        continue
                    if points[i][0] == points[j][0] and points[k][0] == points[l][0] and points[i][0] != points[k][0] and points[i][1] == points[k][1] and points[j][1] == points[l][1] and points[i][1] != points[j][1]:
                        ans += 1
    print(ans//2)

=======
Suggestion 10

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    # x座標でソート
    points.sort()

    # y座標でソート
    points_y = sorted(points, key=lambda x: x[1])

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            # x座標を固定
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2:
                continue

            # y座標がx1からx2の間にある点の個数
            cnt = 0
            for k in range(N):
                x3, y3 = points_y[k]
                if x1 <= x3 <= x2 and y1 <= y3 <= y2:
                    cnt += 1
            ans += cnt * (cnt - 1) // 2

    print(ans)
