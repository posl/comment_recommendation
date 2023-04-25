Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    H = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
    for cx in range(101):
        for cy in range(101):
            Hmax = -1
            for i in range(N):
                if Hmax == -1 and H[i] > 0:
                    Hmax = H[i] + abs(X[i] - cx) + abs(Y[i] - cy)
            if Hmax == -1:
                continue
            flag = True
            for i in range(N):
                if max(Hmax - abs(X[i] - cx) - abs(Y[i] - cy), 0) != H[i]:
                    flag = False
                    break
            if flag:
                print(cx, cy, Hmax)
                return

=======
Suggestion 2

def main():
    N = int(input())
    X = []
    Y = []
    H = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)
    for i in range(101):
        for j in range(101):
            H_max = 0
            for k in range(N):
                if H[k] != 0:
                    H_max = H[k] + abs(X[k] - i) + abs(Y[k] - j)
                    break
            if H_max == 0:
                H_max = 1
            for k in range(N):
                if H[k] != max(H_max - abs(X[k] - i) - abs(Y[k] - j), 0):
                    break
            else:
                print(i, j, H_max)
                return

=======
Suggestion 3

def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    H = [0] * N
    for i in range(N):
        X[i], Y[i], H[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            H0 = -1
            for i in range(N):
                if H[i] > 0:
                    H0 = H[i] + abs(X[i] - cx) + abs(Y[i] - cy)
                    break
            if H0 < 0:
                continue
            for i in range(N):
                if H[i] != max(H0 - abs(X[i] - cx) - abs(Y[i] - cy), 0):
                    break
            else:
                print(cx, cy, H0)
                return

=======
Suggestion 4

def main():
    N = int(input())
    x = [0]*N
    y = [0]*N
    h = [0]*N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            H = -1
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(cx - x[i]) + abs(cy - y[i])
                    break
            if H == -1:
                continue
            for i in range(N):
                if h[i] != max(H - abs(cx - x[i]) - abs(cy - y[i]), 0):
                    break
            else:
                print(cx, cy, H)
                return

=======
Suggestion 5

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
            H = h[0] + abs(x[0] - C_X) + abs(y[0] - C_Y)
            for i in range(1, N):
                if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return

=======
Suggestion 6

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
    for cx in range(101):
        for cy in range(101):
            for hi in range(1, 101):
                if h[0] == 0:
                    continue
                if h[0] != hi + abs(cx - x[0]) + abs(cy - y[0]):
                    continue
                for i in range(1, N):
                    if h[i] != max(hi - abs(cx - x[i]) - abs(cy - y[i]), 0):
                        break
                else:
                    print(cx, cy, hi)
                    return

=======
Suggestion 7

def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        x.append(tmp[0])
        y.append(tmp[1])
        h.append(tmp[2])
    for cx in range(101):
        for cy in range(101):
            H = 0
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(cx - x[i]) + abs(cy - y[i])
                    break
            for i in range(N):
                if h[i] != max(H - abs(cx - x[i]) - abs(cy - y[i]), 0):
                    break
            else:
                print(cx, cy, H)
                return

=======
Suggestion 8

def main():
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    for cx in range(101):
        for cy in range(101):
            h = -1
            for x, y, h0 in data:
                if h0 > 0:
                    h = h0 + abs(x - cx) + abs(y - cy)
                    break
            if h < 0:
                continue
            for x, y, h0 in data:
                if h - abs(x - cx) - abs(y - cy) != h0:
                    break
            else:
                print(cx, cy, h)
                return

=======
Suggestion 9

def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    for x in range(101):
        for y in range(101):
            H = -1
            for i in range(N):
                if data[i][2] > 0:
                    H = data[i][2] + abs(data[i][0] - x) + abs(data[i][1] - y)
                    break
            if H == -1:
                continue
            f = True
            for i in range(N):
                if data[i][2] != max(H - abs(data[i][0] - x) - abs(data[i][1] - y), 0):
                    f = False
                    break
            if f:
                print(x, y, H)
                exit()

=======
Suggestion 10

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    for cx in range(101):
        for cy in range(101):
            for h in range(1000):
                if all([max(h-abs(x-cx)-abs(y-cy),0) == z for x,y,z in A]):
                    print(cx, cy, h)
                    return
