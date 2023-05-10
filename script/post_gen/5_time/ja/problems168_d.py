Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v):
    global seen
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

seen = [False] * (n+1)
dfs(1)

for i in range(1,n+1):
    if not seen[i]:
        print('No')
        exit()

print('Yes')
for i in range(2,n+1):
    print(graph[i][0])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    # 隣接リストを作成
    adj = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        adj[A].append(B)
        adj[B].append(A)

    # BFS
    from collections import deque
    dist = [-1] * N
    dist[0] = 0
    q = deque()
    q.append(0)
    while q:
        v = q.popleft()
        for nv in adj[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)

    # 答えを復元
    ans = [0] * N
    for v in range(N):
        for nv in adj[v]:
            if dist[v] == dist[nv] + 1:
                ans[v] = nv + 1
                break
    print('Yes')
    for v in range(1, N):
        print(ans[v])

=======
Suggestion 3

def check_path(n, m, path):
    # チェック用の配列を作成
    check_list = [0 for i in range(n+1)]
    # 部屋1から出発して、部屋1に戻れるかチェックする
    check_list[1] = 1
    for i in range(m):
        if path[i][0] == 1:
            check_list[path[i][1]] = 1
        elif path[i][1] == 1:
            check_list[path[i][0]] = 1
    for i in range(m):
        if check_list[path[i][0]] == 1:
            check_list[path[i][1]] = 1
        elif check_list[path[i][1]] == 1:
            check_list[path[i][0]] = 1
    for i in range(2, n+1):
        if check_list[i] == 0:
            return False
    return True

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print("-----")
    #グラフ作成
    #隣接リスト作成
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])
    #print(graph)
    #print("-----")
    #BFS
    #初期化
    from collections import deque
    queue = deque()
    queue.append(1)
    visited = [False]*(N+1)
    visited[1] = True
    #print(queue)
    #print(visited)
    #print("-----")
    #探索
    #各部屋からの移動回数を記録
    #部屋1からの移動回数は0
    #各部屋に道しるべを設置する部屋番号を記録
    #部屋1には道しるべを設置しない
    #部屋1の道しるべは、部屋1に設置する
    #道しるべを設置しない場合は-1を記録
    #道しるべの設置は、道しるべを設置する部屋からの移動回数が1増えるごとに行う
    #道しるべを設置する部屋からの移動回数が1増えるごとに、道しるべを設置する部屋からの移動回数を記録する
    #道しるべを設置する部屋からの移動回数が1増えるごとに、道しるべを設置する部屋を記録する
    #道しるべ

=======
Suggestion 5

def dfs(v, g, seen):
    seen[v] = True
    for next_v in g[v]:
        if seen[next_v]:
            continue
        dfs(next_v, g, seen)

=======
Suggestion 6

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

N,M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
seen = [False] * N
dfs(0)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [map(int, input().split()) for _ in range(M)]
    A, B = [list(i) for i in zip(*AB)]

    # 隣接リスト
    adj = [[] for _ in range(N)]
    for a, b in zip(A, B):
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    # BFS
    from collections import deque
    q = deque([0])
    ans = [None] * N
    ans[0] = 0
    while q:
        v = q.popleft()
        for u in adj[v]:
            if ans[u] is None:
                ans[u] = v + 1
                q.append(u)

    print('Yes')
    for a in ans[1:]:
        print(a)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(N,M,A,B)
    #print(A)
    #print(B)
    #print(A[0])
    #print(B[0])
    #print(A[1])
    #print(B[1])
    #print(A[2])
    #print(B[2])
    #print(A[3])
    #print(B[3])
    #print(A[4])
    #print(B[4])
    #print(A[5])
    #print(B[5])
    #print(A[6])
    #print(B[6])
    #print(A[7])
    #print(B[7])
    #print(A[8])
    #print(B[8])
    #print(A[9])
    #print(B[9])
    #print(A[10])
    #print(B[10])
    #print(A[11])
    #print(B[11])
    #print(A[12])
    #print(B[12])
    #print(A[13])
    #print(B[13])
    #print(A[14])
    #print(B[14])
    #print(A[15])
    #print(B[15])
    #print(A[16])
    #print(B[16])
    #print(A[17])
    #print(B[17])
    #print(A[18])
    #print(B[18])
    #print(A[19])
    #print(B[19])
    #print(A[20])
    #print(B[20])
    #print(A[21])
    #print(B[21])
    #print(A[22])
    #print(B[22])
    #print(A[23])
    #print(B[23])
    #print(A[24])
    #print(B[24])
    #print(A[25])
    #print(B[25])
    #print(A[26])
    #print(B[26])
    #print(A[27])
    #print(B[27])
    #print(A[28])
    #print(B[28])
    #print(A[29])
    #print(B[29])
    #print(A[30])
    #print(B[30])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M)
    # print(AB)

    # 部屋の道しるべの番号を格納するリスト
    roadsign = [0] * N

    # 1 からの道しるべを出力
    print('Yes')
    print(1)

    # 部屋 1 以外の道しるべを出力
    # 1 からの道しるべを出力したので、
    # 2 から N までの道しるべを出力
    for i in range(2, N+1):
        print(roadsign[i-1])

        # 道しるべが指す部屋の番号を格納する変数
        # 道しるべが指す部屋の番号は、
        # その部屋と通路で直接つながっている部屋の 1 つ
        roadsign[i-1] = AB[i-2][0]

    # print(roadsign)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M)
    # print(AB)

    # グラフ作成
    # 頂点0は使わない
    # 頂点iは部屋iに対応
    # 辺は部屋間の移動に対応
    # 部屋1からの移動のみを考える
    # 部屋1からの移動を考えると、
    # 1から移動できる部屋、1から移動できる部屋から移動できる部屋、1から移動できる部屋から移動できる部屋から移動できる部屋
    # というように、1から移動できる部屋から移動できる部屋を考えると、1から移動できる部屋から移動できる部屋から移動できる部屋
    # というように、1から移動できる部屋から移動できる部屋を考えると、1から移動できる部屋から移動できる部屋から移動できる部屋
    # というように、1から移動できる部屋から移動できる部屋を考えると、1から移動できる部屋から移動できる部屋から移動できる部屋
    # というように、1から移動できる部屋から移動できる部屋を考えると、1から移動できる部屋から移動できる部屋から移動できる部屋
    # というように、1から移動できる部屋から移動できる部屋を考えると、1から移動できる部屋
