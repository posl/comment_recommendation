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
                    H = h[i] + abs(C_X - x[i]) + abs(C_Y - y[i])
                    break
            for i in range(N):
                if h[i] != max(H - abs(C_X - x[i]) - abs(C_Y - y[i]), 0):
                    break
            else:
                print(C_X, C_Y, H)
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

    ans = [0, 0, 0]
    for cx in range(101):
        for cy in range(101):
            for i in range(N):
                if H[i] != 0:
                    h = H[i] + abs(cx - X[i]) + abs(cy - Y[i])
                    break
            else:
                continue
            for i in range(N):
                if max(h - abs(cx - X[i]) - abs(cy - Y[i]), 0) != H[i]:
                    break
            else:
                ans = [cx, cy, h]
                break
        else:
            continue
        break

    print(*ans)

=======
Suggestion 3

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

    for c_x in range(101):
        for c_y in range(101):
            h = 0
            for i in range(N):
                if H[i] > 0:
                    h = H[i] + abs(c_x - X[i]) + abs(c_y - Y[i])
                    break
            for i in range(N):
                if H[i] != max(h - abs(c_x - X[i]) - abs(c_y - Y[i]), 0):
                    break
            else:
                print(c_x, c_y, h)
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
    for cx in range(101):
        for cy in range(101):
            for h in range(101):
                if h == 0:
                    for i in range(N):
                        if h[i] != 0:
                            break
                    else:
                        print(cx, cy, h)
                        return
                else:
                    for i in range(N):
                        if h[i] != max(h - abs(x[i] - cx) - abs(y[i] - cy), 0):
                            break
                    else:
                        print(cx, cy, h)
                        return

main()

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
            for H in range(1, 1001):
                if h[0] == max(H - abs(x[0] - C_X) - abs(y[0] - C_Y), 0):
                    #print(C_X, C_Y, H)
                    for i in range(N):
                        if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                            break
                        if i == N - 1:
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
    for C_X in range(101):
        for C_Y in range(101):
            for H in range(1, 10**9):
                if h[0] != 0:
                    if h[0] + abs(x[0] - C_X) + abs(y[0] - C_Y) == H:
                        break
                else:
                    if H - abs(x[0] - C_X) - abs(y[0] - C_Y) <= 0:
                        break
            else:
                continue
            break
        else:
            continue
        break
    for i in range(1, N):
        if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
            break
    else:
        print(C_X, C_Y, H)
        return
    print("No Answer")

=======
Suggestion 7

def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        x1, y1, h1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
        h.append(h1)
    for cx in range(101):
        for cy in range(101):
            for i in range(N):
                if h[i] != 0:
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
    data = [list(map(int, input().split())) for i in range(n)]
    for cx in range(101):
        for cy in range(101):
            for h in range(101):
                if all(h == max(h - abs(cx - x) - abs(cy - y), 0) for x, y, h in data):
                    print(cx, cy, h)
                    return

=======
Suggestion 9

def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    #print(data)
    for cx in range(101):
        for cy in range(101):
            h = 0
            for x, y, h0 in data:
                if h0 > 0:
                    h = h0 + abs(x - cx) + abs(y - cy)
                    break
            if h == 0:
                continue
            for x, y, h0 in data:
                if h0 != max(h - abs(x - cx) - abs(y - cy), 0):
                    break
            else:
                print(cx, cy, h)
                return

main()

=======
Suggestion 10

def main():
    N = int(input())

    # 高さが0でない座標を取得
    pos = []
    for i in range(N):
        x, y, h = map(int, input().split())
        if h > 0:
            pos.append((x, y, h))

    # 高さが0でない座標が1つの場合は、その座標を出力
    if len(pos) == 1:
        print(pos[0][0], pos[0][1], pos[0][2])
        return

    # 高さが0でない座標が2つ以上の場合は、全探索
    for cx in range(101):
        for cy in range(101):
            h = pos[0][2] + abs(pos[0][0] - cx) + abs(pos[0][1] - cy)
            for i in range(1, len(pos)):
                if h - abs(pos[i][0] - cx) - abs(pos[i][1] - cy) != pos[i][2]:
                    break
            else:
                print(cx, cy, h)
                return
