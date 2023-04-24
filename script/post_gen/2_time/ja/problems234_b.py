Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

max_dist = 0
for i in range(N):
    for j in range(i + 1, N):
        max_dist = max(max_dist, dist(X[i], Y[i], X[j], Y[j]))
print(max_dist)

=======
Suggestion 2

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, (x[i]-x[j])**2+(y[i]-y[j])**2)
    print(ans**0.5)

=======
Suggestion 3

def main():
    N = int(input())
    xy = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**0.5)
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
    max_dist = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)**0.5
            max_dist = max(max_dist, dist)
    print(max_dist)

=======
Suggestion 5

def main():
    N = int(input())
    P = []
    for i in range(N):
        x,y = map(int,input().split())
        P.append((x,y))

    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,(P[i][0]-P[j][0])**2+(P[i][1]-P[j][1])**2)

    print(ans**0.5)

=======
Suggestion 6

def dist(x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5

=======
Suggestion 7

def main():
    N = int(input())
    #N = 3
    #x = [0,0,1]
    #y = [0,1,1]
    x = []
    y = []
    for i in range(N):
        tmp = input().split()
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    #print(x)
    #print(y)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,(x[i]-x[j])**2+(y[i]-y[j])**2)
    print(ans**0.5)

=======
Suggestion 8

def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append((x, y))
    #print(XY)

    max = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(i, j)
            #print(XY[i], XY[j])
            d = ((XY[i][0]-XY[j][0])**2 + (XY[i][1]-XY[j][1])**2)**0.5
            #print(d)
            if d > max:
                max = d
    print(max)

main()

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    xy = [list(map(int, input().split())) for i in range(N)]
    #最大値の初期化
    max = 0
    #二重ループで全ての組み合わせを試す
    for i in range(N):
        for j in range(i+1,N):
            #長さの計算
            l = ((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)**0.5
            #最大値の更新
            if l > max:
                max = l
    #出力
    print(max)
