Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y = map(int, input().split())
    G = [[0] * N for _ in range(N)]
    for i in range(N - 1):
        G[i][i + 1] = 1
        G[i + 1][i] = 1
    G[X - 1][Y - 1] = 1
    G[Y - 1][X - 1] = 1
    for k in range(1, N):
        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                if G[i][j] == k:
                    ans += 1
        print(ans)

=======
Suggestion 2

def   main (): 
     N ,   X ,   Y   =   map ( int ,   input (). split ()) 
     graph   =   [ []   for   i   in   range ( N )] 
     for   i   in   range ( N - 1 ): 
         graph [ i ]. append ( i + 1 ) 
         graph [ i + 1 ]. append ( i ) 
     graph [ X - 1 ]. append ( Y - 1 ) 
     graph [ Y - 1 ]. append ( X - 1 ) 
     ans   =   [ 0   for   i   in   range ( N - 1 )] 
     for   i   in   range ( N ): 
         dist   =   [ - 1   for   j   in   range ( N )] 
         dist [ i ]   =   0 
         que   =   [ i ] 
         while   que : 
             v   =   que . pop ( 0 ) 
             for   j   in   graph [ v ]: 
                 if   dist [ j ]   ==   - 1 : 
                     dist [ j ]   =   dist [ v ]   +   1 
                     que . append ( j ) 
         for   j   in   range ( i + 1 ,   N ): 
             ans [ dist [ j ] - 1 ]   +=   1 
     for   i   in   range ( N - 1 ): 
         print ( ans [ i ])

=======
Suggestion 3

def main():
    import sys
    input = sys.stdin.readline
    N,X,Y = map(int,input().split())
    X,Y = X-1,Y-1
    ans = [0]*(N-1)
    for i in range(N-1):
        for j in range(i+1,N):
            k = min(j-i,abs(X-i)+1+abs(j-Y),abs(Y-j)+1+abs(i-X))
            ans[k-1] += 1
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    #グラフの作成
    G = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            if j == i+1 or (i+1 == X and j+1 == Y) or (i+1 == Y and j+1 == X):
                G[i][j] = 1
                G[j][i] = 1
    #print(G)
    #距離の計算
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if G[i][k] != 0 and G[k][j] != 0:
                    if G[i][j] == 0 or G[i][j] > G[i][k] + G[k][j]:
                        G[i][j] = G[i][k] + G[k][j]
    #print(G)
    #距離の数え上げ
    for k in range(1,N):
        count = 0
        for i in range(N):
            for j in range(i+1,N):
                if G[i][j] == k:
                    count += 1
        print(count)

=======
Suggestion 5

def   main ():
     N ,  X ,  Y  =  map ( int ,  input (). split ())
     X ,  Y  =  X  -  1 ,  Y  -  1 
     ans  =  [ 0 ] *  N 
     for   i   in   range ( N ):
         for   j   in   range ( i +  1 ,  N ):
             d  =  min ( j - i ,  abs ( X - i ) +  1  +  abs ( j - Y ),  abs ( Y - i ) +  1  +  abs ( j - X ))
             ans [ d ] +=  1 
     for   i   in   range ( 1 ,  N ):
         print ( ans [ i ])

=======
Suggestion 6

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    # 頂点間の距離を格納する2次元配列
    dist = [[0 for _ in range(N)] for _ in range(N)]

    # 頂点間の距離を計算する
    for i in range(N):
        for j in range(i+1, N):
            # 頂点 i と 頂点 j の距離が 1 になるような整数の組 (i,j) (1 ≦ i < j ≦ N) は、
            # (1,2),(2,3),(2,4),(3,4),(4,5) の 5 つです。
            # 頂点 i と 頂点 j の距離が 2 になるような整数の組 (i,j) (1 ≦ i < j ≦ N) は、
            # (1,3),(1,4),(2,5),(3,5) の 4 つです。
            # 頂点 i と 頂点 j の距離が 3 になるような整数の組 (i,j) (1 ≦ i < j ≦ N) は、
            # (1,5) の 1 つだけです。
            # 頂点 i と 頂点 j の距離が 4 になるような整数の組 (i,j) (1 ≦ i < j ≦ N) はありません。
            # 頂点 i と 頂点 j の距離が 5 になるような整数の組 (i,j) (1 ≦ i < j ≦ N) は、
            # (1,6),(1,7),(2,6),(2,7),(3,6),(3,7),(4,6),(4,7),(5,6),(5,7) の 10 つです。
            # 頂点 i

=======
Suggestion 7

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    #グラフの初期化
    graph = [[0] * N for i in range(N)]

    #グラフの作成
    for i in range(N-1):
        graph[i][i+1] = 1
        graph[i+1][i] = 1

    graph[X][Y] = 1
    graph[Y][X] = 1

    #最短経路の探索
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 0 and graph[i][k] > 0 and graph[k][j] > 0:
                    graph[i][j] = graph[i][k] + graph[k][j]

    #距離ごとの整数の組の数の計算
    for k in range(1, N):
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                if graph[i][j] == k:
                    count += 1
        print(count)

=======
Suggestion 8

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    #グラフ作成
    G = [[] for i in range(N)]
    for i in range(N-1):
        G[i].append(i+1)
        G[i+1].append(i)
    G[X-1].append(Y-1)
    G[Y-1].append(X-1)
    #print(G)
    #距離を求める
    for k in range(N-1):
        ans = 0
        for i in range(N):
            for j in range(i+1, N):
                if len(G[i])>len(G[j]):
                    i, j = j, i
                if j in G[i]:
                    ans += 1
                else:
                    for l in range(len(G[i])):
                        if G[i][l] in G[j]:
                            ans += 1
                            break
        print(ans)
        #print(k, ans)

=======
Suggestion 9

def main():
    N, X, Y = map(int, input().split())
    #グラフの作成
    G = [[] for _ in range(N)]
    #頂点 i と 頂点 j の距離が 1 になるような整数の組 (i,j) (1 ≦ i < j ≦ N) は、
    #i+1, i+2, ..., N-1, N, 1, 2, 3, ..., i-1
    #i+1, i+2, ..., N-1, N, 1, 2, 3, ..., i-1
    for i in range(N):
        for j in range(i+1, N):
            if i+1 <= j+1 <= N:
                G[i].append(j)
                G[j].append(i)
            elif i+1 <= j+1-N <= N:
                G[i].append(j+1-N)
                G[j+1-N].append(i)
    #頂点 X と 頂点 Y の間に辺があります
    #X+1 < Y
    G[X-1].append(Y-1)
    G[Y-1].append(X-1)
    #print(G)
    #print()
    #k=1,2,...,N-1 について、以下の問題を解いてください。  
    #整数の組 (i,j) (1 ≦ i < j ≦ N) であって、 G において頂点 i と頂点 j の最短距離が k であるようなものの数を求めてください
    #print(N)
    for k in range(1, N):
        #print(k)
        #print()
        #print(N)
        #print()
        #print(G)
        #print()
        #print()
        #print()
        #print()
        #p

=======
Suggestion 10

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    #print("---------")
    for k in range(1, N):
        #print(k)
        #print("---------")
        count = 0
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                #print(i, j)
                if (abs(i-j) == k) or (abs(i-X) + abs(j-Y) + 1 == k) or (abs(i-Y) + abs(j-X) + 1 == k):
                    count += 1
                    #print("count up")
        print(count)
