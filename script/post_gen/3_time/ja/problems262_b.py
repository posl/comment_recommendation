Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    graph = [[0] * N for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = 1
        graph[v - 1][u - 1] = 1
    ans = 0
    for a in range(N - 2):
        for b in range(a + 1, N - 1):
            for c in range(b + 1, N):
                if graph[a][b] and graph[b][c] and graph[c][a]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    edge = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        edge[u - 1][v - 1] = 1
        edge[v - 1][u - 1] = 1
    ans = 0
    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                if edge[a][b] == 1 and edge[b][c] == 1 and edge[c][a] == 1:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    ans = 0
    for a in range(N):
        for b in edge[a]:
            if a < b:
                for c in edge[b]:
                    if b < c and a in edge[c]:
                        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(M)]

    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            for k in range(j + 1, M):
                if edge[i][0] == edge[j][0] and edge[j][0] == edge[k][0]:
                    continue
                elif edge[i][0] == edge[j][0] and edge[j][0] == edge[k][1]:
                    continue
                elif edge[i][0] == edge[j][1] and edge[j][1] == edge[k][0]:
                    continue
                elif edge[i][0] == edge[j][1] and edge[j][1] == edge[k][1]:
                    continue
                elif edge[i][1] == edge[j][0] and edge[j][0] == edge[k][0]:
                    continue
                elif edge[i][1] == edge[j][0] and edge[j][0] == edge[k][1]:
                    continue
                elif edge[i][1] == edge[j][1] and edge[j][1] == edge[k][0]:
                    continue
                elif edge[i][1] == edge[j][1] and edge[j][1] == edge[k][1]:
                    continue
                else:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    
    graph = [[0] * N for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = 1
        graph[v][u] = 1
    
    ans = 0
    for a in range(N):
        for b in range(a + 1, N):
            if graph[a][b] == 0:
                continue
            for c in range(b + 1, N):
                if graph[b][c] == 0 or graph[c][a] == 0:
                    continue
                ans += 1
    
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    #print(N, M)
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    #print(AB)
    count = 0
    for a in range(1, N):
        for b in range(a+1, N):
            for c in range(b+1, N+1):
                #print(a, b, c)
                if [a, b] in AB and [b, c] in AB and [c, a] in AB:
                    count += 1
    print(count)

=======
Suggestion 7

def main():
    #入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    #グラフを作成
    G = [[] for _ in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    #グラフを探索
    ans = 0
    for a in range(N):
        for b in G[a]:
            if a >= b:
                continue
            for c in G[b]:
                if a >= c:
                    continue
                if c in G[a]:
                    ans += 1
    #出力
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    #辺のリスト
    edges = []
    #頂点のリスト
    nodes = []
    #頂点の次数のリスト
    degrees = [0 for i in range(N)]
    #頂点の次数のリスト
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
        degrees[u - 1] += 1
        degrees[v - 1] += 1
    #次数が2以上の頂点をnodesに追加
    for i in range(N):
        if degrees[i] >= 2:
            nodes.append(i + 1)
    #nodesの要素の組み合わせを全て試す
    ans = 0
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            for k in range(j + 1, len(nodes)):
                if (nodes[i], nodes[j]) in edges and (nodes[j], nodes[k]) in edges and (nodes[k], nodes[i]) in edges:
                    ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    # 1:各頂点に隣接する頂点を格納するリストを作成
    # 2:各頂点に隣接する頂点の数を格納するリストを作成
    # 3:各頂点に隣接する頂点の数の合計を格納するリストを作成
    # 4:隣接する頂点の数の合計の合計を格納する変数を作成
    # 5:隣接する頂点の数の合計の合計を格納する変数を作成
    # 6:隣接する頂点の数の合計の合計を格納する変数を作成
    # 7:隣接する頂点の数の合計の合計を格納する変数を作成
    # 8:隣接する頂点の数の合計の合計を格納する変数を作成
    # 9:隣接する頂点の数の合計の合計を格納する変数を作成
    # 10:隣接する頂点の数の合計の合計を格納する変数を作成
    # 11:隣接する頂点の数の合計の合計を格納する変数を作成
    # 12:隣接する頂点の数の合計の合計を格納する変数を作成
    # 13:隣接する頂点の数の合計の合計を格納する変数を作成
    # 14:隣接する頂点の数の合計の合計を格納する変数を作成
    # 15:隣接する頂点の数の合計の合計を格納する変数を作成
    # 16:隣接

=======
Suggestion 10

def main():
    N, M = map(int, input().split())

    # 2次元リストの初期化
    # 0で初期化
    # 0で初期化したリストをN個作成
    # 0で初期化したリストをN個作成したリストを作成
    # 0で初期化したリストをN個作成したリストを作成したリストを作成
    # 0で初期化したリストをN個作成したリストを作成したリストを作成したリストを作成
    # 0で初期化したリストをN個作成したリストを作成したリストを作成したリストを作成したリストを作成
    # 0で初期化したリストをN個作成したリストを作成したリストを作成したリストを作成したリストを作成したリストを作成
    # 0で初期化したリストをN個作成したリストを作成し�
