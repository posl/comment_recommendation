Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, D = map(int, input().split())
    cnt = 0
    for i in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= D**2:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N, D = map(int, input().split())
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if (x**2 + y**2) <= D**2:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N,D = map(int,input().split())
    count = 0
    for i in range(N):
        x,y = map(int,input().split())
        if x**2+y**2 <= D**2:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N,D = map(int,input().split())
    count = 0
    for i in range(N):
        x,y = map(int,input().split())
        if (x**2 + y**2) <= D**2:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    #入力
    N, D = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    #問題解決
    #原点からの距離がD以下であるような点の個数を求める
    #原点からの距離は(p^2+q^2)^(1/2)で表される
    #Dの2乗
    D2 = D**2
    #原点からの距離がD以下であるような点の個数
    cnt = 0
    for i in range(N):
        #p^2+q^2
        p2q2 = X[i]**2 + Y[i]**2
        if p2q2 <= D2:
            cnt += 1

    #出力
    print(cnt)

=======
Suggestion 7

def main():
    N,D = map(int,input().split())
    ans = 0
    for _ in range(N):
        x,y = map(int,input().split())
        if (x**2 + y**2)**(1/2) <= D:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N, D = map(int, input().split())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    #座標の絶対値がD以下のものを数える
    count = 0
    for i in range(N):
        if (X[i]**2 + Y[i]**2)**(1/2) <= D:
            count += 1
    #出力
    print(count)

=======
Suggestion 9

def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, D = map(int, readline().split())
    X, Y = map(int, read().split())
    ans = 0
    for i in range(N):
        if X**2 + Y**2 <= D**2:
            ans += 1
        X, Y = map(int, readline().split())
    print(ans)

=======
Suggestion 10

def main():
    #入力
    N, D = map(int, input().split())
    #print(N, D)
    #N個の点の座標をリストに格納
    list_xy = []
    for i in range(N):
        X, Y = map(int, input().split())
        list_xy.append([X, Y])
    #print(list_xy)
    #原点からの距離がD以下であるような点の個数をカウント
    count = 0
    for i in range(N):
        if (list_xy[i][0]**2 + list_xy[i][1]**2)**0.5 <= D:
            count += 1
    #出力
    print(count)
