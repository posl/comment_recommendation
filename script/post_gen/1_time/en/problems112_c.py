Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    h = [0] * N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())

    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            for i in range(N):
                if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return

=======
Suggestion 2

def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    h = [0] * n
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            for i in range(n):
                if h[i] != 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            ok = True
            for i in range(n):
                if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                    ok = False
            if ok:
                print(cx, cy, H)
                break

=======
Suggestion 3

def main():
    N = int(input())
    x, y, h = [0] * N, [0] * N, [0] * N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())

    for cx in range(101):
        for cy in range(101):
            H = -1
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            flg = True
            for i in range(N):
                if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                    flg = False
                    break
            if flg:
                print(cx, cy, H)
                return

=======
Suggestion 4

def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        _x, _y, _h = map(int, input().split())
        x.append(_x)
        y.append(_y)
        h.append(_h)

    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            for i in range(N):
                if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return

=======
Suggestion 5

def main():
    n = int(input())
    x,y,h = [],[],[]
    for i in range(n):
        x1,y1,h1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
        h.append(h1)
    for cx in range(0,101):
        for cy in range(0,101):
            H = 0
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
                    break
            for i in range(n):
                if h[i] != max(H - abs(x[i]-cx) - abs(y[i]-cy), 0):
                    break
            else:
                print(cx,cy,H)
                exit()

=======
Suggestion 6

def main():
    n = int(input())
    xyh = [list(map(int, input().split())) for _ in range(n)]
    xyh.sort(key=lambda x: x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            h = xyh[0][2] + abs(xyh[0][0]-cx) + abs(xyh[0][1]-cy)
            for i in range(1, n):
                if xyh[i][2] != max(h - abs(xyh[i][0]-cx) - abs(xyh[i][1]-cy), 0):
                    break
            else:
                print(cx, cy, h)
                return

main()

=======
Suggestion 7

def main():
    N = int(input())
    XYH = [list(map(int, input().split())) for _ in range(N)]
    for cx in range(101):
        for cy in range(101):
            for i in range(N):
                if XYH[i][2] != max(XYH[i][2] + abs(XYH[i][0] - cx) + abs(XYH[i][1] - cy), 0):
                    break
            else:
                print(cx, cy, XYH[i][2] + abs(XYH[i][0] - cx) + abs(XYH[i][1] - cy))
                exit()
    return

=======
Suggestion 8

def check(x,y,h):
    for i in range(n):
        if h!=max(H-abs(X[i]-x)-abs(Y[i]-y),0):
            return False
    return True

n=int(input())
X=[]
Y=[]
H=[]
for i in range(n):
    x,y,h=map(int,input().split())
    X.append(x)
    Y.append(y)
    H.append(h)

for i in range(n):
    if H[i]>0:
        x=X[i]
        y=Y[i]
        h=H[i]
        break

for i in range(101):
    for j in range(101):
        if check(i,j,h):
            print(i,j,h)
            exit()

=======
Suggestion 9

def check(x,y,h):
    for i in range(N):
        if max(h-abs(x-xi[i])-abs(y-yi[i]),0) != hi[i]:
            return False
    return True

N = int(input())
xi = []
yi = []
hi = []
for i in range(N):
    x,y,h = map(int,input().split())
    xi.append(x)
    yi.append(y)
    hi.append(h)

for i in range(N):
    if hi[i] != 0:
        break

x = xi[i]
y = yi[i]
h = hi[i]

for cx in range(101):
    for cy in range(101):
        if check(cx,cy,h):
            print(cx,cy,h)
            exit()

=======
Suggestion 10

def get_center_and_height(n, points):
    for i in range(n):
        if points[i][2] != 0:
            break
    for cx in range(101):
        for cy in range(101):
            h = abs(cx - points[i][0]) + abs(cy - points[i][1]) + points[i][2]
            for j in range(n):
                if max(h - abs(cx - points[j][0]) - abs(cy - points[j][1]), 0) != points[j][2]:
                    break
            else:
                return cx, cy, h

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
print(*get_center_and_height(n, points))
