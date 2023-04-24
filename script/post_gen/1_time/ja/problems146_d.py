Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    #print(G)

    color = [-1] * N

    def dfs(v, p, c):
        color[v] = c
        c = 1
        for u in G[v]:
            if u == p:
                continue
            if c == color[v]:
                c += 1
            dfs(u, v, c)
            c += 1

    dfs(0, -1, 1)
    print(max(color))
    for c in color[1:]:
        print(c)

=======
Suggestion 2

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    c = [0]*N
    def dfs(v,p,cnt):
        for i in G[v]:
            if i == p:
                continue
            cnt += 1
            c[i] = cnt
            dfs(i,v,cnt)
    dfs(0,-1,0)
    print(max(c)+1)
    for i in range(N-1):
        print(c[i+1]+1)

=======
Suggestion 3

def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    colors = [-1]*N
    colors[0] = 1
    stack = [0]
    while stack:
        node = stack.pop()
        color = 1
        for child in edges[node]:
            if colors[child] == -1:
                while color == colors[node]:
                    color += 1
                colors[child] = color
                stack.append(child)
                color += 1
    print(max(colors))
    for i in range(N-1):
        print(colors[i])

=======
Suggestion 4

def   main (): 
     N   =   int ( input ()) 
     G   =   [[]   for   _   in   range ( N + 1 )] 
     for   _   in   range ( N - 1 ): 
         a ,   b   =   map ( int ,   input (). split ()) 
         G [ a ]. append ( b ) 
         G [ b ]. append ( a ) 

     # 頂点の番号を 1 から N にするために -1 する 
     # 0 はダミー 
     color   =   [ 0 ]   *   ( N + 1 ) 
     # 木なので 1 から探索すればよい 
     dfs ( G ,   1 ,   color ) 
     print ( max ( color )) 
     for   i   in   range ( 2 ,   N + 1 ): 
         print ( color [ i ])

=======
Suggestion 5

def   main (): 
     N   =   int ( input ()) 
     G   =   [[]   for   i   in   range ( N )] 
     for   i   in   range ( N   -   1 ): 
         a ,   b   =   map ( int ,   input (). split ()) 
         G [ a   -   1 ]. append ( b   -   1 ) 
         G [ b   -   1 ]. append ( a   -   1 ) 

     # 木の辺を色で塗る
     # 木の辺の塗り分けは、
     # 1. 木の辺を頂点に対応させたグラフの辺の塗り分け
     # 2. 頂点を木の辺に対応させたグラフの辺の塗り分け
     # の2つがあるが、2の方が簡単なので、2の方を考える
     # 2の方を考えると、木の辺を頂点に対応させたグラフの辺の塗り分けは、
     # 木の辺を頂点に対応させたグラフの頂点を辺に対応させたグラフの辺の塗り分けと同値
     # つまり、木の辺を頂点に対応させたグラフの頂点を辺に対応させたグラフの辺の塗り分けが
     # 与えられた時、木の辺を頂点に対応させたグラフの辺の塗り分けは、
     # 木の辺を頂点に対応させたグラフの頂点を辺に対応させたグラフの辺の塗り分けに変換できる
     # 木の辺を頂

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N-1):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    print(N-1)
    for i in range(N-1):
        print(i+1)

=======
Suggestion 7

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    print(N-1)
    for i in range(N-1):
        print(i%N)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N-1)]
    #print(N)
    #print(ab)

    #グラフを作成
    G = [[] for _ in range(N+1)]
    for a, b in ab:
        G[a].append(b)
        G[b].append(a)
    #print(G)

    #深さ優先探索
    #深さ優先探索の実装
    def dfs(v, p, d):
        #print(v, p, d)
        #頂点vを訪れたことを記録
        seen[v] = 1
        #頂点vの深さを記録
        depth[v] = d
        #頂点vに隣接する頂点を探索
        for nv in G[v]:
            #頂点vに隣接する頂点nvが親頂点pでない場合
            if nv != p:
                #頂点nvが未訪問の場合
                if seen[nv] == 0:
                    #頂点nvを訪問済みにする
                    seen[nv] = 1
                    #頂点nvの深さを記録
                    depth[nv] = d + 1
                    #頂点vを親頂点として頂点nvを再帰的に探索
                    dfs(nv, v, d + 1)
                #頂点nvが訪問済みの場合
                else:
                    #頂点nvの深さを記録
                    depth[nv] = d - 1

    #深さ優先探索を実行
    #頂点1を根とする木を探索
    #頂点iを訪れたかどうかを記録する配列
    seen = [0] * (N+1)
    #頂点iの深さを記録する配列
    depth = [

=======
Suggestion 9

def main():
    N = int(input())
    #各頂点の隣接リスト
    edge = [[] for _ in range(N+1)]
    #各頂点の隣接リストを作成
    for _ in range(N-1):
        a,b = map(int,input().split())
        edge[a].append(b)
        edge[b].append(a)
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の塗り分けの色
    color = [0]*(N+1)
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい順にソート
    for i in range(1,N+1):
        edge[i].sort()
    #各頂点の隣接リストを頂点番号の小さい

=======
Suggestion 10

def main():
    N = int(input())
    # a,bの値を格納する
    a = []
    b = []
    for i in range(N-1):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    # 隣接リストを作成
    # 隣接リストの中身は、その頂点に隣接する頂点のリスト
    # 例：隣接リスト[1] = [2,3,4,5,6]
    # 頂点1に隣接する頂点は2,3,4,5,6
    # 頂点1に隣接する頂点は5個
    a_list = [[] for i in range(N+1)]
    # 隣接リストを作成
    for i in range(N-1):
        a_list[a[i]].append(b[i])
        a_list[b[i]].append(a[i])
    # 隣接リストの中身をソート
    for i in range(N+1):
        a_list[i].sort()
    # 頂点1から順番にBFSを行う
    # 訪問済みの頂点を記録する
    # 例：visited[1] = True
    # 頂点1は訪問済み
    visited = [False for i in range(N+1)]
    # 頂点1を訪問済みにする
    visited[1] = True
    # 訪問済みの頂点を格納する
    # 例：queue = [1]
    # 頂点1を訪問済みにしたので、queueに頂点1を格納
    queue = [1]
    # 訪問済みの頂点の色を格納する
    # 例：color[1] = 1
    # 頂点1の色は1
    color = [0 for i in range(N+1)]
    # 訪問済みの頂点の
