Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

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
                    break
            H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
            for i in range(n):
                if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0):
                    break
            else:
                print(cx, cy, H)
                return

=======
Suggestion 3

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
            H = -1
            for i in range(n):
                if h[i] != 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break

            for i in range(n):
                if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0):
                    break
            else:
                print(cx, cy, H)
                return

=======
Suggestion 4

def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    for i in range(N):
        if data[i][2] != 0:
            x, y, h = data[i]
            break
    for C_X in range(101):
        for C_Y in range(101):
            H = h + abs(C_X - x) + abs(C_Y - y)
            for i in range(N):
                if data[i][2] != max(H - abs(C_X - data[i][0]) - abs(C_Y - data[i][1]), 0):
                    break
            else:
                print(C_X, C_Y, H)
                exit()

=======
Suggestion 5

def main():
    # 读取数据
    N = int(input())
    X = [0]*N
    Y = [0]*N
    H = [0]*N
    for i in range(N):
        X[i], Y[i], H[i] = map(int, input().split())

    # 从高度最大的点开始，逐个遍历所有点
    for i in range(N):
        if H[i] > 0:
            cx, cy, ch = X[i], Y[i], H[i]
            break

    # 逐个遍历所有点
    for x in range(101):
        for y in range(101):
            # 当前点的高度
            h = ch + abs(x - cx) + abs(y - cy)
            # 判断当前点是否满足条件
            for i in range(N):
                if H[i] != max(h - abs(x - X[i]) - abs(y - Y[i]), 0):
                    break
            else:
                print(x, y, h)
                return

=======
Suggestion 6

def get_input():
    N = int(input())
    X, Y, H = [], [], []
    for _ in range(N):
        x, y, h = map(int, input().split())
        X.append(x)
        Y.append(y)
        H.append(h)

    return N, X, Y, H

=======
Suggestion 7

def solve():
    #N = int(input())
    #x,y,h = [],[],[]
    #for i in range(N):
    #    x.append(int(input()))
    #    y.append(int(input()))
    #    h.append(int(input()))
    #for cx in range(101):
    #    for cy in range(101):
    #        H = 0
    #        for i in range(N):
    #            if h[i] > 0:
    #                H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
    #                break
    #        flag = True
    #        for i in range(N):
    #            if h[i] != max(H - abs(x[i]-cx) - abs(y[i]-cy), 0):
    #                flag = False
    #                break
    #        if flag:
    #            print(cx, cy, H)
    #            return
    #N = int(input())
    #x,y,h = [],[],[]
    #for i in range(N):
    #    x.append(int(input()))
    #    y.append(int(input()))
    #    h.append(int(input()))
    #for cx in range(101):
    #    for cy in range(101):
    #        H = -1
    #        for i in range(N):
    #            if h[i] > 0:
    #                H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
    #                break
    #        flag = True
    #        for i in range(N):
    #            if h[i] != max(H - abs(x[i]-cx) - abs(y[i]-cy), 0):
    #                flag = False
    #                break
    #        if flag:
    #            print(cx, cy, H)
    #            return
    N = int(input())
    x,y,h = [],[],[]
    for i in range(N):
        x.append(int(input()))
        y.append(int(input()))
        h.append(int(input()))
    for cx in range(101):
        for cy in range(101):
            H = -1
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i]-cx) + abs(y[i]-cy)
                    break
            flag

=======
Suggestion 8

def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        h.append(c)
    for i in range(101):
        for j in range(101):
            for k in range(n):
                if h[k] != 0:
                    H = abs(x[k] - i) + abs(y[k] - j) + h[k]
                    break
            for k in range(n):
                if h[k] != max(H-abs(x[k]-i)-abs(y[k]-j), 0):
                    break
            else:
                print(i, j, H)
                return

=======
Suggestion 9

def problems112_c():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)

    # 从高度最高的点开始遍历，找到第一个高度不为0的点，即为中心点
    for i in range(N):
        if h[i] != 0:
            center_x = x[i]
            center_y = y[i]
            height = h[i]
            break

    # 从中心点开始遍历，判断每个点的高度是否满足条件
    for i in range(101):
        for j in range(101):
            # 如果该点高度为0，则跳过
            if h[i] == 0:
                continue
            # 如果该点的高度不等于height-|i-center_x|-|j-center_y|，则跳过
            if h[i] != height - abs(i-center_x) - abs(j-center_y):
                continue
            # 如果该点的高度等于height-|i-center_x|-|j-center_y|，则继续判断
            if h[i] == height - abs(i-center_x) - abs(j-center_y):
                continue

    print(center_x, center_y, height)

problems112_c()
