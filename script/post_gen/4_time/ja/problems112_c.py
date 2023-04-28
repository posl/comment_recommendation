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
                if h[i] != 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            ok = True
            for i in range(N):
                if max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0) != h[i]:
                    ok = False
                    break
            if ok:
                print(C_X, C_Y, H)
                return

=======
Suggestion 2

def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    h = [0] * N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())
    for C_X in range(101):
        for C_Y in range(101):
            H = h[0] + abs(x[0] - C_X) + abs(y[0] - C_Y)
            if all(h[i] == max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0) for i in range(N)):
                print(C_X, C_Y, H)
                return

=======
Suggestion 3

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
                if h[i] == 0:
                    continue
                else:
                    tmp = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    if H == 0:
                        H = tmp
                    elif H != tmp:
                        break
            else:
                print(C_X, C_Y, H)
                exit()

=======
Suggestion 4

def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    H = [0] * N
    for i in range(N):
        X[i], Y[i], H[i] = map(int, input().split())

    for cx in range(101):
        for cy in range(101):
            H0 = 0
            for i in range(N):
                if H[i] != 0:
                    H0 = H[i] + abs(X[i] - cx) + abs(Y[i] - cy)
                    break
            for i in range(N):
                if max(H0 - abs(X[i] - cx) - abs(Y[i] - cy), 0) != H[i]:
                    break
            else:
                print(cx, cy, H0)
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
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(C_X - x[i]) + abs(C_Y - y[i])
                    break
            flag = True
            for i in range(n):
                if max(H - abs(C_X - x[i]) - abs(C_Y - y[i]), 0) != h[i]:
                    flag = False
                    break
            if flag:
                print(C_X, C_Y, H)
                return

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        x_, y_, h_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        h.append(h_)
    for cx in range(101):
        for cy in range(101):
            for i in range(n):
                if h[i] != 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            for i in range(n):
                if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                    break
            else:
                print(cx, cy, H)
                return

=======
Suggestion 7

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
            for i in range(N):
                if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                exit()

=======
Suggestion 8

def main():
    N = int(input())
    x, y, h = [], [], []
    for i in range(N):
        x_, y_, h_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        h.append(h_)

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
Suggestion 9

def get_pyramid_center_and_height(N, x, y, h):
    for cx in range(101):
        for cy in range(101):
            H = h[0] + abs(x[0] - cx) + abs(y[0] - cy)
            if H > 0:
                for i in range(1, N):
                    if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0):
                        break
                else:
                    return cx, cy, H
    return None, None, None

=======
Suggestion 10

def main():
    N = int(input())
    #print(N)
    data = []
    for i in range(N):
        #print(i)
        data.append(input())
        #print(data[i])
    #print(data)
    
    for i in range(N):
        data[i] = data[i].split()
        #print(data[i])
        data[i] = list(map(int, data[i]))
        #print(data[i])
    
    #print(data)
    
    for i in range(N):
        if data[i][2] > 0:
            C_X = data[i][0]
            C_Y = data[i][1]
            H = data[i][2]
            #print(C_X, C_Y, H)
            break
    
    for x in range(101):
        for y in range(101):
            #print(x, y)
            H = H + abs(x - C_X) + abs(y - C_Y)
            #print(H)
            for i in range(N):
                #print(i)
                if data[i][2] != max(H - abs(x - data[i][0]) - abs(y - data[i][1]), 0):
                    #print(data[i][2])
                    #print(max(H - abs(x - data[i][0]) - abs(y - data[i][1]), 0))
                    break
                if i == N - 1:
                    print(x, y, H)
                    exit()
