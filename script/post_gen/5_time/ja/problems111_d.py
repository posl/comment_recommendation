Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    X, Y = zip(*XY)
    if sum([X[i] == X[i + 1] and Y[i] == Y[i + 1] for i in range(N - 1)]) == N - 1:
        print(-1)
        return
    for m in range(1, 41):
        for d in range(1, 10 ** 12 + 1):
            if m * d < max(abs(max(X)), abs(max(Y))):
                continue
            if m * d < max(abs(min(X)), abs(min(Y))):
                continue
            if m * d > max(abs(max(X)), abs(max(Y))):
                continue
            if m * d > max(abs(min(X)), abs(min(Y))):
                continue
            if m * d > max(abs(max(X)), abs(max(Y))):
                continue
            if m * d > max(abs(min(X)), abs(min(Y))):
                continue
            break
        else:
            continue
        break
    else:
        print(-1)
        return
    print(m)
    print(*[d] * m)
    for x, y in XY:
        ans = []
        for i in range(m):
            if x < 0:
                ans.append('L')
                x += d
            else:
                ans.append('R')
                x -= d
        for i in range(m):
            if y < 0:
                ans.append('D')
                y += d
            else:
                ans.append('U')
                y -= d
        print(*ans, sep='')

=======
Suggestion 3

def main():
    import sys
    readline = sys.stdin.readline

    # 入力
    N = int(readline())
    XY = [list(map(int, readline().split())) for _ in range(N)]

    # 処理
    # すべての点について、x座標とy座標が同じであるか
    x_same = True
    y_same = True
    for x, y in XY:
        if x != XY[0][0]:
            x_same = False
        if y != XY[0][1]:
            y_same = False

    if x_same == False and y_same == False:
        print(-1)
        return

    # x座標が同じ
    if x_same:
        # x座標が同じなら、y座標の差が奇数である
        y_diff = [abs(y - XY[0][1]) for x, y in XY]
        y_diff_odd = [y for y in y_diff if y % 2 == 1]
        if len(y_diff_odd) > 0 and len(y_diff_odd) < len(y_diff):
            print(-1)
            return

        # 差が奇数である場合、y座標が同じになるようにする
        if len(y_diff_odd) > 0:
            for i in range(N):
                if y_diff[i] % 2 == 0:
                    XY[i][1] += 1
                    y_diff[i] += 1
                    break

        # y座標の差を2で割ったものが、ロボットアームの本数
        m = max(y_diff) // 2
        d = [2 * m - y for y in y_diff]
        w = []
        for x, y in XY:
            w_j = ''
            for i in range(m):
                if y > 0:
                    w_j += 'D'
                    y -= 1
                else:
                    w_j += 'U'
                    y += 1
            w.append(w_j)

    # y座標が同じ
    if y

=======
Suggestion 4

def check(x,y):
    return x+y

=======
Suggestion 5

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    x = [xy[i][0] for i in range(n)]
    y = [xy[i][1] for i in range(n)]
    m = 40
    d = [0] * m
    w = [[''] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            dx = x[j] - x[i]
            dy = y[j] - y[i]
            if dx >= 0 and dy >= 0:
                w[i][j] = 'R' * dx + 'U' * dy
            elif dx >= 0 and dy < 0:
                w[i][j] = 'R' * dx + 'D' * (-dy)
            elif dx < 0 and dy >= 0:
                w[i][j] = 'L' * (-dx) + 'U' * dy
            else:
                w[i][j] = 'L' * (-dx) + 'D' * (-dy)
    for i in range(m):
        d[i] = 10 ** 12
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d[i] = min(d[i], len(w[i][j]))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if len(w[i][j]) == d[i]:
                w[i][j] = w[i][j][:-1]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if len(w[i][j]) < d[i]:
                w[i][j] += w[j][i]
                w[i][j] += w[i][j][0] * (d[i] - len(w[i][j]))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if len(w[i][j]) > d[i]:
                w[i][j] = w[i][j][:d[i]]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

=======
Suggestion 6

def main():
    return

=======
Suggestion 7

def solve():
    N = int(input())
    XY = [list(map(int,input().split())) for _ in range(N)]
    #print(N,XY)
    #print(XY[0][0])
    #print(XY[0][1])
    #print(XY[1][0])
    #print(XY[1][1])
    #print(XY[2][0])
    #print(XY[2][1])
    #print(XY[3][0])
    #print(XY[3][1])
    #print(XY[4][0])
    #print(XY[4][1])


    #print(XY[0][0])
    #print(XY[0][1])
    #print(XY[1][0])
    #print(XY[1][1])
    #print(XY[2][0])
    #print(XY[2][1])
    #print(XY[3][0])
    #print(XY[3][1])
    #print(XY[4][0])
    #print(XY[4][1])
    #print(XY[5][0])
    #print(XY[5][1])
    #print(XY[6][0])
    #print(XY[6][1])
    #print(XY[7][0])
    #print(XY[7][1])

    #print(XY[0][0])
    #print(XY[0][1])
    #print(XY[1][0])
    #print(XY[1][1])
    #print(XY[2][0])
    #print(XY[2][1])
    #print(XY[3][0])
    #print(XY[3][1])
    #print(XY[4][0])
    #print(XY[4][1])
    #print(XY[5][0])
    #print(XY[5][1])
    #print(XY[6][0])
    #print(XY[6][1])
    #print(XY[7][0])
    #print(XY[7][1])
    #print(XY[8][0])
    #print(XY[8][1])
    #print(XY[9][0])
    #print(XY[9][1])
    #print(XY[10][

=======
Suggestion 8

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)

    if n == 1:
        print(1)
        print(1)
        print("L")
        exit()
    if n == 2:
        if x[0] == x[1] and y[0] == y[1]:
            print(1)
            print(1)
            print("L")
        else:
            print(2)
            print(1, 1)
            print("RL")
            print("LR")
        exit()

    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print(2)
                print(1, 1)
                print("RL")
                print("LR")
                exit()

    print(3)
    print(1, 1, 1)
    print("RLD")
    print("LDR")
    print("DRU")

=======
Suggestion 9

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    #print(xy)
    #print("-----")

    # 1. mを決める
    # 2. dを決める
    # 3. wを決める

    # 1. mを決める
    # mは、全てのxy座標の中で最大の座標の値を取る
    # ただし、最小値は1とする
    # つまり、最大値が10^9なら、mは10^9となる
    # また、最小値が-10^9なら、mは10^9となる
    # なお、mの最大値は40となる

    # 2. dを決める
    # dは、全てのxy座標の中で最大の座標の値を取る
    # ただし、最小値は1とする
    # つまり、最大値が10^9なら、dは10^9となる
    # また、最小値が-10^9なら、dは10^9となる
    # なお、dの最大値は10^12となる

    # 3. wを決める
    # wは、mの数だけ必要となる
    # wは、全てのxy座標の中で最大の座標の値を取る
    # ただし、最小値は1とする
    # つまり、最大値が10^9なら、wは10^9となる
    # また、最小値が-10^9なら、wは10^9となる
    # なお、wの最大値は40となる

    # 4. 1,2,3を満たすか確
