Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            dx = X[i] - X[j]
            dy = Y[i] - Y[j]
            ans = max(ans, abs(dx) + abs(dy))
    print(ans + 1)

=======
Suggestion 2

def main():
    n = int(input())
    x, y = [0] * n, [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())

    # 2点間の距離を計算
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2

    # 2点間の距離が等しいものの個数を数える
    d = {}
    for i in range(n):
        for j in range(i + 1, n):
            if dist[i][j] in d:
                d[dist[i][j]] += 1
            else:
                d[dist[i][j]] = 1

    # 2点間の距離が等しいものが2個以上あれば、
    # 2点間の距離が等しいものの個数が答え
    for v in d.values():
        if v >= 2:
            print(v + 1)
            return

    # 2点間の距離が等しいものが1個もなければ、
    # 2点間の距離が等しいものがないので、
    # 2点間の距離が等しいものの個数は1
    print(1)

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    x.sort()
    y.sort()
    ans = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                ans += abs(x[i] - x[j]) + abs(y[i] - y[j])
    ans //= N
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i],Y[i] = map(int,input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans,abs(X[i]-X[j])+abs(Y[i]-Y[j]))
    print(ans)

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    # 魔法は整数の組 (a,b) によって識別されていて、地点 (x,y) にいるときに魔法 (a,b) を使うと (x+a,y+b) にワープする
    # すぬけ君は、任意の整数の組 (a,b) を選んで魔法 (a,b) を覚えることができる大魔術師
    # すぬけ君は何種類でも魔法を覚えることができる
    # 魔法を使って街と街の間を移動したくなったすぬけ君は、全ての相異なる街の組 (i,j) について次の行動を取れるようにいくつかの魔法を覚えることにしました。
    # 覚えた魔法のうち 1 種類の魔法のみ を選ぶ。その後、選んだ魔法 のみ を繰り返し使って街 i から 街 j に移動する。
    # すぬけ君が上の条件を満たすように魔法を覚えるとき、少なくとも何種類の魔法を覚えればよいか？
    # 2 ≦ N ≦ 500
    # 0 ≦ x_i ≦ 10^9 (1 ≦ i ≦ N)
    # 0 ≦ y_i ≦ 10^9 (1 ≦ i ≦ N)
    # i ≠ j ならば (x_i, y_i) ≠ (x_j, y_j) である。
    # 同じ

=======
Suggestion 7

def main():
    import sys
    readline = sys.stdin.readline
    read = sys.stdin.read
    #n = int(readline())
    n, *xy = map(int, read().split())
    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = xy[2*i], xy[2*i+1]
            x2, y2 = xy[2*j], xy[2*j+1]
            d[(x2-x1, y2-y1)] += 1
            d[(x1-x2, y1-y2)] += 1
    print(n - max(d.values()))

=======
Suggestion 8

def main():
    N = int(input())
    XY = []
    for i in range(N):
        XY.append(list(map(int, input().split())))
    #print(XY)

    #各街の座標から、他の街の座標までの移動距離を計算する
    #移動距離をキー、移動距離の出現回数を値とした辞書を作成する
    #移動距離の出現回数が2以上の場合、移動距離の出現回数を値とした辞書を作成する
    #移動距離の出現回数が2以上の辞書をリストに格納する
    #移動距離の出現回数が2以上の辞書のリストの長さを出力する

    #移動距離の出現回数が2以上の辞書をリストに格納する
    #移動距離の出現回数が2以上の辞書のリストの長さを出力する
    #移動距離の出現回数が2以上の辞書のリストの長さが0の場合、N*(N-1)/2を出力する
    #移動距離の出現回数が2以上の辞書のリストの長さが1の場合、移動距離の出現回数が2以上の辞書のリストの長さを出力する
    #移動距離の出現回数が2以上の辞書のリストの長さが2の場合、移動距離の出現回数が2以上の辞書のリストの長さを出力する
    #移動距離の出現回数が2以上の辞書のリストの長さが

=======
Suggestion 9

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    # 2点間の距離の差が同じなら、その2点間は魔法を使って移動できる
    # 2点間の距離の差が異なるなら、その2点間は魔法を使って移動できない
    # 2点間の距離の差は、x座標の差とy座標の差の絶対値の和
    # 2点間の距離の差が同じなら、その2点間は魔法を使って移動できる
    # 2点間の距離の差が異なるなら、その2点間は魔法を使って移動できない
    # 2点間の距離の差は、x座標の差とy座標の差の絶対値の和
    # 2点間の距離の差が同じなら、その2点間は魔法を使って移動できる
    # 2点間の距離の差が異なるなら、その2点間は魔法を使って移動できない
    # 2点間の距離の差は、x座標の差とy座標の差の絶対値の和
    # 2点間の距離の差が同じなら、その2点間は魔法を使って移動できる
    # 2点間の距離の差が異なるなら、その2点間は魔法を使って移動できない
    # 2点間の距離の差は、x座標の
