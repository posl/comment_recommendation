Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    H = []
    for i in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
    for cx in range(101):
        for cy in range(101):
            for h in range(101):
                if h == 0:
                    if (cx, cy) in zip(X, Y):
                        continue
                    else:
                        break
                flag = True
                for x, y, hh in zip(X, Y, H):
                    if h != hh + abs(x - cx) + abs(y - cy):
                        flag = False
                        break
                if flag:
                    print(cx, cy, h)
                    return

=======
Suggestion 2

def main():
    N = int(input())
    X = []
    Y = []
    H = []
    for i in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)

    for cx in range(101):
        for cy in range(101):
            Hmax = 0
            for i in range(N):
                if H[i] != 0:
                    Hmax = H[i] + abs(cx - X[i]) + abs(cy - Y[i])
                    break
            for i in range(N):
                if H[i] != max(Hmax - abs(cx - X[i]) - abs(cy - Y[i]), 0):
                    break
            else:
                print(cx, cy, Hmax)
                return

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h[i] != 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            if H == 0:
                H = 1
            for i in range(N):
                if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return

=======
Suggestion 4

def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)
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
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        x_, y_, h_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        h.append(h_)
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h[i] != 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            for i in range(N):
                if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    y = []
    h = []
    for _ in range(n):
        x1, y1, h1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
        h.append(h1)
    #print(x)
    #print(y)
    #print(h)

    #h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y|, 0) となるC_X, C_Y, Hを求める
    #h[i] = 0の場合はC_X, C_Y, Hの候補としては考慮しない
    #h[i] = 0でない場合はC_X, C_Y, Hの候補として考慮する
    #h[i]が0でない場合について、h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y|, 0)を満たすC_X, C_Y, Hの候補を求める
    #h[i]が0でない場合について、h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y|, 0)を満たすC_X, C_Y, Hの候補を求める
    #h[i]が0でない場合について、h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y|, 0)を満たすC_X, C_Y, Hの候補を求める
    #h[i]が0でない場合について、h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y|, 0)を満たすC_X, C_Y, Hの候補を求める
    #h[i]が0でない場合について、h[i] = max(H - |x[i] - C_X| - |y[i] - C_Y

=======
Suggestion 7

def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: x[2], reverse=True)
    for C_X in range(101):
        for C_Y in range(101):
            H = data[0][2] + abs(data[0][0] - C_X) + abs(data[0][1] - C_Y)
            for i in range(1, N):
                if H - abs(data[i][0] - C_X) - abs(data[i][1] - C_Y) != data[i][2]:
                    break
            else:
                print(C_X, C_Y, H)
                return

=======
Suggestion 8

def main():
    N = int(input())
    XYH = [list(map(int, input().split())) for _ in range(N)]
    XYH.sort(key=lambda x: x[2], reverse=True)
    for x in range(101):
        for y in range(101):
            h = XYH[0][2] + abs(XYH[0][0] - x) + abs(XYH[0][1] - y)
            for i in range(N):
                if XYH[i][2] != max(h - abs(XYH[i][0] - x) - abs(XYH[i][1] - y), 0):
                    break
            else:
                print(x, y, h)
                return

=======
Suggestion 9

def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    for x in range(101):
        for y in range(101):
            H = -1
            for i in range(N):
                if data[i][2] > 0:
                    H = data[i][2] + abs(x - data[i][0]) + abs(y - data[i][1])
                    break
            if H == -1:
                continue
            flag = True
            for i in range(N):
                if max(H - abs(x - data[i][0]) - abs(y - data[i][1]), 0) != data[i][2]:
                    flag = False
                    break
            if flag:
                print(x, y, H)
                return

=======
Suggestion 10

def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    for cx in range(101):
        for cy in range(101):
            h = 0
            for x, y, h0 in data:
                if h0 == 0:
                    continue
                h = h0 + abs(cx - x) + abs(cy - y)
                break
            for x, y, h0 in data:
                if h0 != max(h - abs(cx - x) - abs(cy - y), 0):
                    break
            else:
                print(cx, cy, h)
                return
