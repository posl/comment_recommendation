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
    for C_X in range(101):
        for C_Y in range(101):
            H0 = 0
            for i in range(N):
                if H[i] > 0:
                    H0 = H[i] + abs(X[i] - C_X) + abs(Y[i] - C_Y)
                    break
            for i in range(N):
                if H[i] != max(H0 - abs(X[i] - C_X) - abs(Y[i] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H0)
                return

=======
Suggestion 2

def main():
    n = int(input())
    x_list = []
    y_list = []
    h_list = []
    for i in range(n):
        x, y, h = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
        h_list.append(h)
    for cx in range(101):
        for cy in range(101):
            h = 0
            for i in range(n):
                if h_list[i] != 0:
                    tmp_h = h_list[i] + abs(x_list[i] - cx) + abs(y_list[i] - cy)
                    if h == 0:
                        h = tmp_h
                    elif h != tmp_h:
                        h = -1
                        break
            if h != -1:
                print(cx, cy, h)
                return

=======
Suggestion 3

def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    h = [0]*n

    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())

    for cx in range(101):
        for cy in range(101):
            H = -1
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
Suggestion 4

def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        h.append(c)

    for i in range(N):
        if h[i] != 0:
            x1 = x[i]
            y1 = y[i]
            h1 = h[i]
            break

    for C_X in range(101):
        for C_Y in range(101):
            H = h1 + abs(C_X - x1) + abs(C_Y - y1)
            flag = True
            for i in range(N):
                if h[i] != max(H - abs(C_X - x[i]) - abs(C_Y - y[i]), 0):
                    flag = False
                    break
            if flag == True:
                print(C_X, C_Y, H)
                break
        if flag == True:
            break

=======
Suggestion 5

def main():
    n = int(input())
    x, y, h = [], [], []
    for i in range(n):
        _x, _y, _h = map(int, input().split())
        x.append(_x)
        y.append(_y)
        h.append(_h)

    for cx in range(101):
        for cy in range(101):
            H = -1
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            flag = True
            for i in range(n):
                if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                    flag = False
                    break
            if flag:
                print(cx, cy, H)
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

    for C_X in range(101):
        for C_Y in range(101):
            H = -1
            for i in range(N):
                if h[i] > 0:
                    tmp = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    if H == -1:
                        H = tmp
                    elif H != tmp:
                        break
            else:
                print(C_X, C_Y, H)
                return

=======
Suggestion 7

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
    for cx in range(101):
        for cy in range(101):
            H = 0
            for i in range(N):
                if h[i] != 0:
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
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        X, Y, H = map(int, input().split())
        x.append(X)
        y.append(Y)
        h.append(H)
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    break
            for i in range(N):
                if max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0) != h[i]:
                    break
            else:
                print(C_X, C_Y, H)
                exit()

=======
Suggestion 9

def main():
    n = int(input())
    xyh = []
    for _ in range(n):
        xyh.append(list(map(int, input().split())))
    xyh.sort(key=lambda x: x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            height = xyh[0][2] + abs(xyh[0][0] - cx) + abs(xyh[0][1] - cy)
            for i in range(1, n):
                if xyh[i][2] != max(height - abs(xyh[i][0] - cx) - abs(xyh[i][1] - cy), 0):
                    break
            else:
                print(cx, cy, height)
                return

=======
Suggestion 10

def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input()
    # input_lineを半角スペースで分割して、input_lineに上書き
    input_line = input_line.split(" ")
    # input_lineをint型に変換して、input_lineに上書き
    input_line = list(map(int, input_line))
    # input_lineの各要素を変数に代入
    N = input_line[0]
    x = input_line[1]
    y = input_line[2]
    h = input_line[3]
    # ここから問題を解く
    # N個の情報から、中心座標と高さを特定する
    # その中心座標と高さを出力する
    for i in range(N):
        input_line = input()
        input_line = input_line.split(" ")
        input_line = list(map(int, input_line))
        x_i = input_line[0]
        y_i = input_line[1]
        h_i = input_line[2]
        if h_i > 0:
            cx = x_i
            cy = y_i
            ch = h_i
    print(cx, cy, ch)
