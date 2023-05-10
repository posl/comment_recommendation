Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    x = [0] * 5
    for i in range(N):
        t, x[i], a = map(int, input().split())
        x[i] -= 1
    x.sort()
    ans = 0
    for i in range(1, N):
        if x[i] - x[i-1] > 1:
            ans += x[i] - x[i-1] - 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    #print(txa)
    ans = 0
    for i in range(n):
        t, x, a = txa[i][0], txa[i][1], txa[i][2]
        if i == 0:
            ans = a
        else:
            ans = max(ans + a, a)
        if i != n - 1:
            t_next, x_next = txa[i+1][0], txa[i+1][1]
            if t_next - t >= abs(x_next - x):
                ans = max(ans, a)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    #print(N, T, X, A)
    #print(len(T), len(X), len(A))

    # T[i]の時刻にX[i]の位置にA[i]の大きさのすぬけが出現
    # T[i]の時刻にX[i]の位置に高橋がいるとき、高橋はすぬけを捕獲できる
    # すぬけを捕獲するとき、高橋は1秒で1以上の距離を移動することができる
    # すぬけを捕獲するとき、高橋は最適な行動をとる
    # 捕獲できるすぬけの大きさの合計の最大値を求める

    # 1. すぬけが出現する時間順にソートする
    # 2. すぬけが出現する位置順にソートする
    # 3. すぬけを捕獲する
    # 4. 捕獲できるすぬけの大きさの合計の最大値を求める

    # 1. すぬけが出現する時間順にソートする
    # 2. すぬけが出現する位置順にソートする
    # 3. すぬけを捕獲する
    # 4. 捕獲できるすぬけの大きさの合計の最大値を求める

    # 1. すぬけが出現する時間順にソートする
    # 2.

=======
Suggestion 4

def main():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    txa.insert(0, [0, 0, 0])
    txa.append([10**5, 0, 0])
    #print(txa)
    #print(n)
    #print(txa[1][0])
    #print(txa[2][0])
    #print(txa[3][0])
    #print(txa[4][0])
    #print(txa[5][0])
    #print(txa[6][0])
    #print(txa[7][0])
    #print(txa[8][0])
    #print(txa[9][0])
    #print(txa[10][0])
    #print(txa[11][0])
    #print(txa[12][0])

    #print(txa[1][1])
    #print(txa[2][1])
    #print(txa[3][1])
    #print(txa[4][1])
    #print(txa[5][1])
    #print(txa[6][1])
    #print(txa[7][1])
    #print(txa[8][1])
    #print(txa[9][1])
    #print(txa[10][1])
    #print(txa[11][1])
    #print(txa[12][1])

    #print(txa[1][2])
    #print(txa[2][2])
    #print(txa[3][2])
    #print(txa[4][2])
    #print(txa[5][2])
    #print(txa[6][2])
    #print(txa[7][2])
    #print(txa[8][2])
    #print(txa[9][2])
    #print(txa[10][2])
    #print(txa[11][2])
    #print(txa[12][2])

    #print(txa[1][0] - txa[0][0])
    #print(txa[2][0] - txa[1][0])
    #print(txa[3][0] - txa[2][0])
    #print(txa[4][0] - txa[3][0

=======
Suggestion 5

def main():
    n = int(input())
    txa = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    t = 0
    x = 0
    for i in range(n):
        ans = max(ans, txa[i][2])
        if txa[i][2] > txa[i][0] - t + abs(txa[i][1] - x):
            ans = max(ans, (txa[i][2] + txa[i][0] - t + abs(txa[i][1] - x)) // 2)
        t = txa[i][0]
        x = txa[i][1]
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = []
    for i in range(N):
        t,x,a = map(int,input().split())
        A.append((t,x,a))
    A.sort()
    ans = 0
    now = 0
    for a in A:
        t,x,a = a
        if now < x:
            now = x
        if now + a > t:
            ans += a
            now += a
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    data = []
    for i in range(n):
        t,x,a = map(int,input().split())
        data.append([t,x,a])
    data = sorted(data)
    ans = 0
    for i in range(n):
        t,x,a = data[i]
        if x == 0:
            ans += a
        else:
            for j in range(i):
                t0,x0,a0 = data[j]
                if t0 + abs(x0-x) <= t:
                    ans += a
                    break
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    txa = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        t, x, a = txa[i]
        ans += a
        if i < n-1:
            t2, x2, a2 = txa[i+1]
            ans -= max(0, t2 - (t + abs(x2 - x)))
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())

    # 各穴に出てくる最大のすぬけ君の大きさを求める
    # すぬけ君は時刻順に出てくるため、時刻が同じ場合は大きい方を採用する
    max_A = [0] * 5
    for i in range(N):
        max_A[X[i]] = max(max_A[X[i]], A[i])

    # 時刻 0 から 4 までの移動時間を求める
    # 移動時間は、移動先の座標の差分の絶対値
    # ただし、移動時間が 1 未満の場合は 1 とする
    move_time = [0] * 5
    for i in range(4):
        move_time[i+1] = max(1, abs(i - (i+1)))

    # 移動時間と穴に出てくる最大のすぬけ君の大きさを掛け合わせたものの合計が答え
    ans = 0
    for i in range(5):
        ans += max_A[i] * move_time[i]
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    #print(N)
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
        #print(T, X, A)

    #print(T, X, A)
    #print(len(T))
    #print(len(X))
    #print(len(A))

    #print(T[0])
    #print(X[0])
    #print(A[0])
    #print(T[1])
    #print(X[1])
    #print(A[1])
    #print(T[2])
    #print(X[2])
    #print(A[2])
    #print(T[3])
    #print(X[3])
    #print(A[3])
    #print(T[4])
    #print(X[4])
    #print(A[4])
    #print(T[5])
    #print(X[5])
    #print(A[5])
    #print(T[6])
    #print(X[6])
    #print(A[6])
    #print(T[7])
    #print(X[7])
    #print(A[7])
    #print(T[8])
    #print(X[8])
    #print(A[8])
    #print(T[9])
    #print(X[9])
    #print(A[9])

    #print(T[0])
    #print(T[1])
    #print(T[2])
    #print(T[3])
    #print(T[4])
    #print(T[5])
    #print(T[6])
    #print(T[7])
    #print(T[8])
    #print(T[9])

    #print(X[0])
    #print(X[1])
    #print(X[2])
    #print(X[3])
    #print(X[4])
    #print(X[5])
    #print(X[6])
    #print(X[7])
    #print(X[8])
    #print(X[9])

    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A
