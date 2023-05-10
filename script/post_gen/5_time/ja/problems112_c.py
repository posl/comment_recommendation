Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x, y, h = [], [], []
    for i in range(n):
        x_, y_, h_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        h.append(h_)
    for cx in range(101):
        for cy in range(101):
            H = []
            for i in range(n):
                if h[i] > 0:
                    H.append(h[i] + abs(x[i] - cx) + abs(y[i] - cy))
            if len(set(H)) == 1:
                print(cx, cy, H[0])
                exit()

=======
Suggestion 2

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
    for cx in range(101):
        for cy in range(101):
            H = 0
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i] - cx) + abs(y[i] - cy)
                    break
            for i in range(n):
                if max(H - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]:
                    break
            else:
                print(cx, cy, H)
                exit()

=======
Suggestion 3

def main():
    n = int(input())
    xyz = [list(map(int, input().split())) for i in range(n)]

    for i in range(101):
        for j in range(101):
            h = xyz[0][2] + abs(xyz[0][0] - i) + abs(xyz[0][1] - j)
            if all(max(h - abs(xyz[k][0] - i) - abs(xyz[k][1] - j), 0) == xyz[k][2] for k in range(n)):
                print(i, j, h)
                break

=======
Suggestion 4

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
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(n):
                if h[i] > 0:
                    H = h[i] + abs(x[i]-C_X) + abs(y[i]-C_Y)
                    break
            flag = True
            for i in range(n):
                if max(H-abs(x[i]-C_X)-abs(y[i]-C_Y), 0) != h[i]:
                    flag = False
                    break
            if flag:
                print(C_X, C_Y, H)
                exit()

=======
Suggestion 5

def main():
    N = int(input())
    xyh = [list(map(int, input().split())) for _ in range(N)]
    xyh.sort(key=lambda x:x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            H = xyh[0][2] + abs(cx - xyh[0][0]) + abs(cy - xyh[0][1])
            for i in range(1, N):
                if xyh[i][2] != max(H - abs(cx - xyh[i][0]) - abs(cy - xyh[i][1]), 0):
                    break
            else:
                print(cx, cy, H)
                return

=======
Suggestion 6

def check(x,y,h):
    for i in range(n):
        if h != max(H - abs(x - X[i]) - abs(y - Y[i]), 0):
            return False
    return True

n = int(input())
X = [0] * n
Y = [0] * n
H = [0] * n
for i in range(n):
    X[i], Y[i], H[i] = map(int, input().split())

for i in range(n):
    if H[i] != 0:
        break

for x in range(101):
    for y in range(101):
        h = H[i] + abs(x - X[i]) + abs(y - Y[i])
        if check(x,y,h):
            print(x,y,h)
            break

=======
Suggestion 7

def main():
    print("Hello World")

=======
Suggestion 8

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
                    H = h[i] + abs(C_X - x[i]) + abs(C_Y - y[i])
                    break
            for i in range(N):
                if h[i] != max(H - abs(C_X - x[i]) - abs(C_Y - y[i]), 0):
                    break
                if i == N - 1:
                    print(C_X, C_Y, H)
                    return

=======
Suggestion 9

def main():
    #n = int(input())
    #a, b = map(int, input().split())
    #s = input()
    n = int(input())
    xyz = []
    for i in range(n):
        x, y, h = map(int, input().split())
        xyz.append([x, y, h])
    xyz.sort(key=lambda x: x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            H = xyz[0][2] + abs(xyz[0][0] - cx) + abs(xyz[0][1] - cy)
            if all([max(H - abs(xyz[i][0] - cx) - abs(xyz[i][1] - cy), 0) == xyz[i][2] for i in range(n)]):
                print(cx, cy, H)
                exit()

=======
Suggestion 10

def main():
    # 1行目の入力を取得
    N = int(input())
    # 2行目以降の入力を取得
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    #print(data)

    # ピラミッドの中心座標と高さを特定する
    for i in range(N):
        if data[i][2] != 0:
            C_X = data[i][0]
            C_Y = data[i][1]
            H = data[i][2]
            break

    #print(C_X, C_Y, H)

    # ピラミッドの中心座標と高さを特定する
    for i in range(101):
        for j in range(101):
            #print(i, j)
            #print(data[0][2] + abs(data[0][0] - i) + abs(data[0][1] - j))
            #print(data[1][2] + abs(data[1][0] - i) + abs(data[1][1] - j))
            #print(data[2][2] + abs(data[2][0] - i) + abs(data[2][1] - j))
            #print(data[3][2] + abs(data[3][0] - i) + abs(data[3][1] - j))
            #print(data[4][2] + abs(data[4][0] - i) + abs(data[4][1] - j))

            for k in range(N):
                if data[k][2] != max(H - abs(data[k][0] - i) - abs(data[k][1] - j), 0):
                    break
            else:
                print(i, j, max(H - abs(data[k][0] - i) - abs(data[k][1] - j), 0))
                exit()
