Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()

    # compute
    XY.sort()
    XY = list(map(list, zip(*XY)))
    Xs = XY[0]
    Ys = XY[1]
    if (Xs[0] < Xs[-1] and S.count('L') == 0) or (Xs[0] > Xs[-1] and S.count('R') == 0):
        print('No')
    elif (Ys[0] < Ys[-1] and S.count('D') == 0) or (Ys[0] > Ys[-1] and S.count('U') == 0):
        print('No')
    else:
        print('Yes')

=======
Suggestion 2

def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    #print(N, XY, S)

    # 人iが歩く軌跡のリスト
    # 人iの軌跡は、人iの初期座標と、人iの歩く方向をリストに入れておく
    # 人iの歩く方向は、Rなら右、Lなら左を1として、-1をかけておく
    # 人iの歩く方向は、1つ前の人の歩く方向と逆になる
    # 人iの歩く方向は、人iの歩く軌跡のリストの最後の要素の2番目で表現する
    # 人iの歩く軌跡のリストの最後の要素の1番目は、その人の初期座標である
    # 人iの歩く軌跡のリストの最後の要素の2番目は、その人の歩く方向である
    # 人iの歩く軌跡のリストの最後の要素の3番目は、その人の歩く軌跡のリストの長さである
    # 人iの歩く軌跡のリストの最後の要素の4番目は、その人の歩く軌跡のリストの最初の要素のインデックスである
    # 人iの歩く軌跡のリストの最後の要素の5番目は、その人の歩く軌跡のリストの最後の要素のインデックスである
    # 人iの歩く軌跡のリストの最後の要素の6番目は、その人の歩く軌

=======
Suggestion 3

def main():
    N = int(input())
    X = []
    Y = []
    S = input()
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    for i in range(N):
        if S[i] == "R":
            X1.append(X[i])
            Y1.append(Y[i])
        else:
            X2.append(X[i])
            Y2.append(Y[i])
    X1.sort()
    Y1.sort()
    X2.sort()
    Y2.sort()
    if X1[-1] < X2[0] or Y1[-1] < Y2[0] or X2[-1] < X1[0] or Y2[-1] < Y1[0]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()

    # X座標とY座標のリストを作る
    X = [x for x, y in XY]
    Y = [y for x, y in XY]

    # 左右の向きを判定する
    is_right = [s == 'R' for s in S]

    # X座標とY座標をそれぞれソートする
    X.sort()
    Y.sort()

    # X座標とY座標の差分をとる
    X_diff = [X[i + 1] - X[i] for i in range(N - 1)]
    Y_diff = [Y[i + 1] - Y[i] for i in range(N - 1)]

    # 左右の向きによって、差分の正負を変える
    for i in range(N - 1):
        if not is_right[i]:
            X_diff[i] *= -1
        if not is_right[i + 1]:
            Y_diff[i] *= -1

    # 差分が正負が逆になっている場合は衝突する
    if (all([x > 0 for x in X_diff]) and all([y < 0 for y in Y_diff])) or (all([x < 0 for x in X_diff]) and all([y > 0 for y in Y_diff])):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N = int(input())
    XY = [list(map(int,input().split())) for _ in range(N)]
    S = input()
    for i in range(N):
        if S[i] == 'R':
            XY[i][1] += 1
        else:
            XY[i][1] -= 1
    XY.sort()
    #print(XY)
    for i in range(N-1):
        if XY[i][1] == XY[i+1][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 6

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    s = input()

    # 右向きの人と左向きの人を分けて考える
    # 同じ向きの人同士は衝突しないので、
    # 右向きの人の中でy座標が一番小さい人と
    # 左向きの人の中でy座標が一番大きい人が衝突する
    # また、右向きの人の中でy座標が一番大きい人と
    # 左向きの人の中でy座標が一番小さい人が衝突する

    # 右向きの人の中でy座標が一番小さい人
    right_min = 10**9
    right_min_index = 0
    for i in range(n):
        if s[i] == "R":
            if xy[i][1] < right_min:
                right_min = xy[i][1]
                right_min_index = i
    # 左向きの人の中でy座標が一番大きい人
    left_max = 0
    left_max_index = 0
    for i in range(n):
        if s[i] == "L":
            if xy[i][1] > left_max:
                left_max = xy[i][1]
                left_max_index = i

    # 右向きの人の中でy座標が一番大きい人
    right_max = 0
    right_max_index = 0
    for i in range(n):
        if s[i] == "R":
            if xy[i][1] > right_max:
                right_max = xy[i][1]
                right_max_index = i
    # 左向きの人の中でy座標が一番小さい人
    left_min = 10**9
    left_min_index = 0
    for i in range(n):
        if s[i] == "L":
            if

=======
Suggestion 7

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    s = input()
    print(x)
    print(y)
    print(s)
    # x = [2, 1, 4]
    # y = [3, 1, 1]
    # s = "RRL"
    # x = [1, 2]
    # y = [1, 1]
    # s = "RR"
    # x = [1, 1, 0, 0, 0, 3, 2, 4, 4, 3]
    # y = [3, 4, 0, 2, 4, 1, 4, 2, 4, 3]
    # s = "RLRRRLRLRR"
    # x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # s = "RRRRRRRRRR"
    # x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # s = "LLLLLLLLLL"
    # x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # s = "RLRLRLRLRL"
    # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # y = [1, 1, 1, 1, 1, 1, 1, 1,

=======
Suggestion 8

def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()

    x_min = 10**9
    x_max = 0
    y_min = 10**9
    y_max = 0
    for i in range(N):
        if S[i] == 'R':
            x_min = min(x_min, XY[i][0])
        elif S[i] == 'L':
            x_max = max(x_max, XY[i][0])
        elif S[i] == 'U':
            y_min = min(y_min, XY[i][1])
        elif S[i] == 'D':
            y_max = max(y_max, XY[i][1])

    if x_min > x_max or y_min > y_max:
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    s = input()
    x = []
    y = []
    for i in range(n):
        x.append(xy[i][0])
        y.append(xy[i][1])
    for i in range(n):
        if s[i] == "R":
            x[i] += 1
        elif s[i] == "L":
            x[i] -= 1
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 10

def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()

    # 各人の移動方向を初期化
    dir = [0] * N
    for i, s in enumerate(S):
        if s == 'R':
            dir[i] = 1
        else:
            dir[i] = -1

    # 各人の移動先を初期化
    X = [0] * N
    Y = [0] * N
    for i, xy in enumerate(XY):
        X[i] = xy[0]
        Y[i] = xy[1]

    # 各人の移動先を計算
    for i in range(N):
        X[i] += dir[i]
        Y[i] += dir[i]

    # 移動先の座標でソート
    X.sort()
    Y.sort()

    # 移動先の座標が同じ人がいたら衝突する
    for i in range(N-1):
        if X[i] == X[i+1] or Y[i] == Y[i+1]:
            print('Yes')
            exit()

    # 衝突しなかったら衝突しない
    print('No')
