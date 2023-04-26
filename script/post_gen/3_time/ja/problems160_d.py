Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(N-1):
        G[i].append(i+1)
        G[i+1].append(i)
    G[X-1].append(Y-1)
    G[Y-1].append(X-1)
    for k in range(1, N):
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                if len(G[i]) == k and len(G[j]) == k:
                    count += 1
        print(count)

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    for k in range(1, N):
        ans = 0
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                if (i == X and j == Y) or (i == Y and j == X):
                    continue
                if abs(i-j) <= k:
                    ans += 1
                if abs(i-X) + abs(j-Y) <= k:
                    ans += 1
                if abs(i-Y) + abs(j-X) <= k:
                    ans += 1
        print(ans//2)

=======
Suggestion 3

def main():
    N, X, Y = map(int, input().split())
    for k in range(1, N):
        ans = 0
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                if i < X and X < j < Y and j - i == k:
                    ans += 1
                elif X < i < Y and Y < j and j - i == k:
                    ans += 1
                elif i < X and X < j < Y and j - i == k + 1:
                    ans += 1
                elif X < i < Y and Y < j and j - i == k + 1:
                    ans += 1
                elif i < X and X < j < Y and j - i > k + 1:
                    ans += 2
                elif X < i < Y and Y < j and j - i > k + 1:
                    ans += 2
                elif i < X and X < j < Y and j - i < k:
                    ans += 0
                elif X < i < Y and Y < j and j - i < k:
                    ans += 0
                elif i < X and X < j < Y and j - i == k:
                    ans += 1
                elif X < i < Y and Y < j and j - i == k:
                    ans += 1
                elif i < X and X < j < Y and j - i == k + 1:
                    ans += 1
                elif X < i < Y and Y < j and j - i == k + 1:
                    ans += 1
                elif i < X and X < j < Y and j - i > k + 1:
                    ans += 2
                elif X < i < Y and Y < j and j - i > k + 1:
                    ans += 2
                elif i < X and X < j < Y and j - i < k:
                    ans += 0
                elif X < i < Y and Y < j and j - i < k:
                    ans += 0
        print(ans)

=======
Suggestion 4

def main():
    N,X,Y = map(int,input().split())
    #1 から N までの番号がつけられた N 個の頂点を持つ無向グラフ G がある。
    #G には、以下のように合計 N 本の辺がある。
    #i=1,2,...,N-1 について、頂点 i と頂点 i+1 の間に辺がある。
    #頂点 X と頂点 Y の間に辺がある。
    #k=1,2,...,N-1 について、以下の問題を解く。
    #整数の組 (i,j) (1 ≦ i < j ≦ N) であって、 G において頂点 i と頂点 j の最短距離が k であるようなものの数を求める。
    #print(N,X,Y)
    #print("")

    #整数の組 (i,j) (1 ≦ i < j ≦ N) であって、 G において頂点 i と頂点 j の最短距離が k であるようなものの数を求める。
    #これは、各頂点からの距離を求めて、それをリストに格納して、その中でkになっているものを数える。
    #これは、各頂点からの距離を求めて、それをリストに格納する。
    #これは、各頂点

=======
Suggestion 5

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    G = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if i == X and j == Y:
                G[i][j] = 1
                G[j][i] = 1
                continue
            if i == Y and j == X:
                G[i][j] = 1
                G[j][i] = 1
                continue
            if i + 1 == j:
                G[i][j] = 1
                G[j][i] = 1
                continue
            if j + 1 == i:
                G[i][j] = 1
                G[j][i] = 1
                continue
    for k in range(1, N):
        ans = 0
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if G[i][j] == k:
                    ans += 1
        print(ans)

=======
Suggestion 6

def main():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    ans = [0] * (N-1)
    for i in range(N):
        for j in range(i+1,N):
            d = min(j-i,abs(X-i)+1+abs(j-Y))
            ans[d-1] += 1
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 7

def main():
    N,X,Y = map(int,input().split())
    ans = [0 for i in range(N-1)]
    for i in range(1,N):
        for j in range(i+1,N+1):
            if i == X and j == Y:
                ans[min(j-i-1,N-j+i-1)] += 1
            else:
                ans[min(j-i-1,abs(X-i)+1+abs(Y-j))] += 1
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 8

def main():
    N, X, Y = map(int, input().split())
    #N, X, Y = 10, 4, 8
    #N, X, Y = 3, 1, 3
    #N, X, Y = 7, 3, 7
    #N, X, Y = 5, 2, 4
    #N, X, Y = 10, 4, 8

    #辺のリスト
    edges = []
    #頂点iと頂点jの距離がkの場合の整数の組(i,j)の数を格納するリスト
    distance = [0] * (N-1)
    #print("distance:", distance)

    #辺のリストを作成
    for i in range(1, N):
        edges.append((i, i+1))
    edges.append((X, Y))
    #print("edges:", edges)

    #辺のリストから頂点iと頂点jの距離を求め、distanceに格納
    for edge in edges:
        #print("edge:", edge)
        distance[abs(edge[0] - edge[1]) - 1] += 1
    #print("distance:", distance)

    #distanceの要素を出力
    for d in distance:
        print(d)

=======
Suggestion 9

def main():
    n,x,y = map(int,input().split())
    a = [0] * n
    for i in range(1,n):
        for j in range(i+1,n+1):
            a[min(j-i,abs(x-i)+1+abs(y-j))] += 1
    for i in range(1,n):
        print(a[i])

=======
Suggestion 10

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    # 頂点の数
    #print(N)
    # 頂点Xと頂点Yの間に辺がある
    #print(X, Y)
    # 頂点iと頂点jの間に辺がある
    #print(i, j)
    # 頂点iと頂点jの最短距離がkである
    #print(k)
    # 整数の組(i,j) であって、Gにおいて頂点iと頂点jの最短距離がkであるようなものの数を求める
    #print(cnt)
    #print("")
