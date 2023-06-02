Synthesizing 10/10 solutions

=======
Suggestion 1

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
            for H in range(101):
                flag = True
                for i in range(N):
                    if h[i] != max(H-abs(x[i]-C_X)-abs(y[i]-C_Y),0):
                        flag = False
                        break
                if flag:
                    print(C_X,C_Y,H)
                    return

=======
Suggestion 2

def main():
    n = int(input())
    xyh = [list(map(int,input().split())) for i in range(n)]
    for i in range(101):
        for j in range(101):
            for k in range(n):
                if xyh[k][2] != 0:
                    H = xyh[k][2] + abs(xyh[k][0]-i) + abs(xyh[k][1]-j)
                    break
            for k in range(n):
                if xyh[k][2] != max(H-abs(xyh[k][0]-i)-abs(xyh[k][1]-j),0):
                    break
            else:
                print(i,j,H)
                return

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        x1, y1, h1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
        h.append(h1)
    for cx in range(101):
        for cy in range(101):
            for k in range(n):
                if h[k] > 0:
                    break
            H = h[k] + abs(x[k] - cx) + abs(y[k] - cy)
            flag = True
            for k in range(n):
                if h[k] != max(H - abs(x[k] - cx) - abs(y[k] - cy), 0):
                    flag = False
                    break
            if flag:
                print(cx, cy, H)
                return

=======
Suggestion 4

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    points.sort(key=lambda x: x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            for i in range(n):
                x, y, h = points[i]
                if h != 0:
                    H = h + abs(x - cx) + abs(y - cy)
                    break
            else:
                continue
            for i in range(n):
                x, y, h = points[i]
                if h != max(H - abs(x - cx) - abs(y - cy), 0):
                    break
            else:
                print(cx, cy, H)
                return

=======
Suggestion 5

def main():
    print("Hello, World!")

=======
Suggestion 6

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
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(n):
                if h[i] != 0:
                    H = h[i] + abs(C_X - x[i]) + abs(C_Y - y[i])
                    break
            for i in range(n):
                if h[i] != max(H - abs(C_X - x[i]) - abs(C_Y - y[i]), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return

=======
Suggestion 7

def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    h = [0] * n
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            H = 0
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            for i in range(n):
                if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0):
                    break
            else:
                print(cx, cy, H)
                return

=======
Suggestion 8

def main():
    N = int(input())
    x, y, h = [], [], []
    for i in range(N):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        h.append(c)
    for Cx in range(101):
        for Cy in range(101):
            H = -1
            for i in range(N):
                if h[i] > 0:
                    tmp = h[i] + abs(x[i] - Cx) + abs(y[i] - Cy)
                    if H == -1:
                        H = tmp
                    elif H != tmp:
                        break
            else:
                print(Cx, Cy, H)
                return

=======
Suggestion 9

def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        a,b,c = map(int,input().split())
        x.append(a)
        y.append(b)
        h.append(c)
    
    for C_X in range(0,101):
        for C_Y in range(0,101):
            H = 0
            for i in range(n):
                if h[i] != 0:
                    H = h[i] + abs(x[i]-C_X) + abs(y[i]-C_Y)
                    break
            for i in range(n):
                if h[i] != max(H - abs(x[i]-C_X) - abs(y[i]-C_Y),0):
                    break
            else:
                print(C_X,C_Y,H)
                return

=======
Suggestion 10

def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    h = [0]*n
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
                    break
            for i in range(n):
                if h[i] != max(H-abs(x[i]-cx)-abs(y[i]-cy), 0):
                    break
            else:
                print(cx, cy, H)
                exit()
