Synthesizing 10/10 solutions

=======
Suggestion 1

def get_center(x1,y1,h1,x2,y2,h2,x3,y3,h3):
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1
    if h1 == h2:
        h4 = h3
    elif h1 == h3:
        h4 = h2
    else:
        h4 = h1
    return x4,y4,h4

N = int(input())
x = []
y = []
h = []
for i in range(N):
    x1,y1,h1 = map(int, input().split())
    x.append(x1)
    y.append(y1)
    h.append(h1)
for j in range(N):
    if h[j] > 0:
        x4,y4,h4 = get_center(x[0],y[0],h[0],x[1],y[1],h[1],x[j],y[j],h[j])
        break
print(x4,y4,h4)

=======
Suggestion 2

def main():
    n = int(input())
    x = [0 for i in range(n)]
    y = [0 for i in range(n)]
    h = [0 for i in range(n)]
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            if h[0] != 0:
                H = h[0] + abs(x[0] - cx) + abs(y[0] - cy)
                break
    for cx in range(101):
        for cy in range(101):
            for i in range(n):
                if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0):
                    break
            else:
                print(cx, cy, H)
                exit()

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
                if h[i] > 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            for i in range(N):
                if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                exit()

=======
Suggestion 4

def func(N, x, y, h):
    for C_X in range(101):
        for C_Y in range(101):
            H = h[0] + abs(x[0] - C_X) + abs(y[0] - C_Y)
            if H > 0:
                break
        if H > 0:
            break
    for i in range(N):
        if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
            return False
    return C_X, C_Y, H

=======
Suggestion 5

def main():
    N = int(input())
    x_list = [0]*N
    y_list = [0]*N
    h_list = [0]*N
    for i in range(N):
        x_list[i],y_list[i],h_list[i] = map(int,input().split())
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h_list[i] > 0:
                    H = h_list[i] + abs(x_list[i]-C_X) + abs(y_list[i]-C_Y)
                    break
            for i in range(N):
                if h_list[i] != max(H - abs(x_list[i]-C_X) - abs(y_list[i]-C_Y),0):
                    break
            else:
                print(C_X,C_Y,H)
                return

=======
Suggestion 6

def main():
    n = int(input())
    x,y,h = [],[],[]
    for i in range(n):
        a,b,c = map(int,input().split())
        x.append(a)
        y.append(b)
        h.append(c)
    for cx in range(101):
        for cy in range(101):
            H = 0
            for i in range(n):
                if h[i] != 0:
                    H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
                    break
            for i in range(n):
                if h[i] != max(H - abs(x[i]-cx) - abs(y[i]-cy),0):
                    break
            else:
                print(cx,cy,H)
                return

main()

=======
Suggestion 7

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    h = [0] * N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())
    for cx in range(101):
        for cy in range(101):
            H = 0
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            for i in range(N):
                if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                    break
            else:
                print(cx, cy, H)
                return

=======
Suggestion 8

def main():
    n = int(input())
    x, y, h = [], [], []
    for i in range(n):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)
    for C_X in range(101):
        for C_Y in range(101):
            H = -1
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            for i in range(n):
                if max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0) != h[i]:
                    break
            else:
                print(C_X, C_Y, H)
                exit()

=======
Suggestion 9

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
                ok = True
                H_0 = 0
                for i in range(N):
                    if h[i] > 0:
                        H_0 = max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0)
                        break
                for i in range(N):
                    if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0) + H_0:
                        ok = False
                        break
                if ok:
                    print(C_X, C_Y, H)
                    exit()

=======
Suggestion 10

def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        x1,y1,h1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
        h.append(h1)
    for cx in range(101):
        for cy in range(101):
            H = 0
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            for i in range(n):
                if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy),0):
                    break
            else:
                print(cx,cy,H)
                return
