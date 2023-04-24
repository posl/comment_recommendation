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
            Hmax = 0
            for i in range(N):
                if H[i] > 0:
                    Hmax = H[i] + abs(X[i] - cx) + abs(Y[i] - cy)
                    break
            for i in range(N):
                if H[i] != max(Hmax - abs(X[i] - cx) - abs(Y[i] - cy), 0):
                    break
            else:
                print(cx, cy, Hmax)
                exit()

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
    for cx in range(101):
        for cy in range(101):
            h = H[0] + abs(cx - X[0]) + abs(cy - Y[0])
            for i in range(1, N):
                if H[i] != max(h - abs(cx - X[i]) - abs(cy - Y[i]), 0):
                    break
            else:
                print(cx, cy, h)
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
    
    for i in range(101):
        for j in range(101):
            H = h[0] + abs(x[0] - i) + abs(y[0] - j)
            for k in range(1, N):
                if h[k] != max(H - abs(x[k] - i) - abs(y[k] - j), 0):
                    break
            else:
                print(i, j, H)
                break

=======
Suggestion 4

def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)
    for cx in range(101):
        for cy in range(101):
            for h0 in range(1, 101):
                if h[0] == 0:
                    h0 = 0
                for i in range(n):
                    if h[i] != max(h0 - abs(x[i] - cx) - abs(y[i] - cy), 0):
                        break
                    if i == n - 1:
                        print(cx, cy, h0)
                        return

=======
Suggestion 5

def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)
    for c_x in range(101):
        for c_y in range(101):
            h_0 = h[0] + abs(c_x - x[0]) + abs(c_y - y[0])
            if h_0 < 0:
                continue
            for i in range(1, n):
                if h[i] != max(h_0 - abs(c_x - x[i]) - abs(c_y - y[i]), 0):
                    break
            else:
                print(c_x, c_y, h_0)
                return

=======
Suggestion 6

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y, h = map(int, input().split())
        points.append((x, y, h))
    for cx in range(101):
        for cy in range(101):
            h = max([p[2] + abs(p[0] - cx) + abs(p[1] - cy) for p in points if p[2] > 0])
            if all([max(h - abs(p[0] - cx) - abs(p[1] - cy), 0) == p[2] for p in points]):
                print(cx, cy, h)
                return

=======
Suggestion 7

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y, h = map(int, input().split())
        points.append((x, y, h))
    points = sorted(points, key=lambda x: x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            h = points[0][2] + abs(points[0][0] - cx) + abs(points[0][1] - cy)
            for x, y, h0 in points[1:]:
                if h0 != max(h - abs(x - cx) - abs(y - cy), 0):
                    break
            else:
                print(cx, cy, h)
                return

=======
Suggestion 8

def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    for C_X in range(101):
        for C_Y in range(101):
            for i in range(N):
                if data[i][2] > 0:
                    H = data[i][2] + abs(data[i][0] - C_X) + abs(data[i][1] - C_Y)
                    break
            for i in range(N):
                if data[i][2] != max(H - abs(data[i][0] - C_X) - abs(data[i][1] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return

=======
Suggestion 9

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    for cx in range(101):
        for cy in range(101):
            h = 0
            for x, y, h0 in points:
                if h0 > 0:
                    h = h0 + abs(cx - x) + abs(cy - y)
                    break
            for x, y, h0 in points:
                if h - abs(cx - x) - abs(cy - y) != h0:
                    break
            else:
                print(cx, cy, h)
                return

=======
Suggestion 10

def main():
    N = int(input())
    #N = 3
    #x = [99, 100, 99]
    #y = [1, 1, 0]
    #h = [191, 192, 192]
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
            for H in range(1, max(h)+1):
                if h[0] == H - abs(x[0]-C_X) - abs(y[0]-C_Y):
                    flag = 1
                    for i in range(1, N):
                        if h[i] != max(H - abs(x[i]-C_X) - abs(y[i]-C_Y), 0):
                            flag = 0
                            break
                    if flag == 1:
                        print(C_X, C_Y, H)
                        return 0
