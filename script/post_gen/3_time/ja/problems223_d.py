Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #条件を満たすパターンを作成
    #Aが先にくるパターン
    #Bが先にくるパターン
    #AとBが同時にくるパタ��

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 1. A[i] < B[i]の場合、A[i]はB[i]よりも先に現れる
    # 2. A[i] > B[i]の場合、A[i]はB[i]よりも後に現れる
    # 3. A[i] = B[i]の場合、A[i]とB[i]の順番は変わらない

    # 1.を満たすように並び替える
    # 1.を満たすように並び替えることができない場合は、-1を出力する

    # 1.を満たすように並び替える
    # 1.を満たすように並び替えることができない場合は、-1を出力する

    # 1.を満たすように並び替える
    # 1.を満たすように並び替えることができない場合は、-1を出力する

    # 1.を満たすように並び替える
    # 1.を満たすように並び替えることができない場合は、-1を出力する

    # 1.を満たすように並び替える
    # 1.を満たすように並び替えることができない場合は、-1を出力する

    # 1.を満たすように並び替える
    # 1.を満たすように並び替える

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)

    # トポロジカルソート
    # 1. 入次数が 0 の頂点を取り出す
    # 2. その頂点から出ている辺を削除
    # 3. 1 に戻る
    # 4. 2 ができなくなったら終了

    # 入次数を数える
    in_deg = [0] * n
    for i in range(n):
        for j in graph[i]:
            in_deg[j] += 1

    # 入次数が 0 の頂点をスタックに追加
    stack = []
    for i in range(n):
        if in_deg[i] == 0:
            stack.append(i)

    # トポロジカルソート
    res = []
    while stack:
        v = stack.pop()
        res.append(v)
        for i in graph[v]:
            in_deg[i] -= 1
            if in_deg[i] == 0:
                stack.append(i)

    # グラフに閉路がある場合は -1 を出力する
    if len(res) != n:
        print(-1)
    else:
        print(*[r + 1 for r in res])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(lambda x: int(x) - 1, input().split())
        graph[A].append(B)

    # トポロジカルソート
    # 入次数を求める
    in_deg = [0] * N
    for i in range(N):
        for j in range(len(graph[i])):
            in_deg[graph[i][j]] += 1

    # 入次数0の頂点をキューに入れる
    que = []
    for i in range(N):
        if in_deg[i] == 0:
            que.append(i)

    # キューが空になるまで繰り返す
    ans = []
    while que:
        # キューから頂点を取り出す
        v = que.pop(0)
        ans.append(v)
        # 頂点vから出ている辺を削除
        for i in range(len(graph[v])):
            in_deg[graph[v][i]] -= 1
            # 新たに入次数0となった頂点をキューに入れる
            if in_deg[graph[v][i]] == 0:
                que.append(graph[v][i])

    if len(ans) != N:
        print(-1)
    else:
        print(*map(lambda x: x + 1, ans))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        adj[A].append(B)
    P = []
    visited = [False] * (N+1)
    def dfs(v):
        visited[v] = True
        for u in adj[v]:
            if visited[u]:
                return False
            if not dfs(u):
                return False
        P.append(v)
        return True
    for v in range(1, N+1):
        if not visited[v] and not dfs(v):
            print(-1)
            return
    print(*P)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    #print(N, M)
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A, B)
    #N, M = 4, 3
    #A = [2, 3, 2]
    #B = [1, 4, 4]
    #N, M = 2, 3
    #A = [1, 1, 2]
    #B = [2, 2, 1]
    
    # 1. A[i] < B[i] となるように並び替える
    # 2. A[i] < B[i] となるように並び替える
    # 3. A[i] < B[i] となるように並び替える
    # 4. A[i] < B[i] となるように並び替える
    # 5. A[i] < B[i] となるように並び替える
    # 6. A[i] < B[i] となるように並び替える
    # 7. A[i] < B[i] となるように並び替える
    # 8. A[i] < B[i] となるように並び替える
    # 9. A[i] < B[i] となるように並び替える
    # 10. A[i] < B[i] となるように並び替える
    # 11. A[i] < B[i] となるように並び替える
    # 12. A[i] < B[i] となるように並び替える
    # 13. A[i] < B[i] となるように並

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = []
    for i in range(1, N+1):
        ans.append(i)
    for i in range(M-1, -1, -1):
        a = AB[i][0]
        b = AB[i][1]
        if ans.index(a) > ans.index(b):
            ans.remove(a)
            ans.insert(ans.index(b), a)
    if len(set(ans)) == N:
        print(*ans)
    else:
        print(-1)

=======
Suggestion 8

def main():
    # 入力
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 出力
    print(-1)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * N
    for a, b in AB:
        if ans[a - 1] == 0 and ans[b - 1] == 0:
            ans[a - 1] = b
            ans[b - 1] = a
        elif ans[a - 1] == 0:
            ans[a - 1] = b
        elif ans[b - 1] == 0:
            ans[b - 1] = a
        else:
            print(-1)
            return
    for i in range(N):
        if ans[i] == 0:
            ans[i] = i + 1
    print(*ans)

=======
Suggestion 10

def main():
    #入力
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]

    #グラフの初期化
    graph = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)
    #グラフの構築
    for a,b in AB:
        graph[a].append(b)
        in_degree[b] += 1

    #トポロジカルソート
    res = []
    que = []
    for i in range(1,N+1):
        if in_degree[i] == 0:
            que.append(i)

    while que:
        v = que.pop()
        res.append(v)
        for nv in graph[v]:
            in_degree[nv] -= 1
            if in_degree[nv] == 0:
                que.append(nv)

    #出力
    if len(res) != N:
        print(-1)
    else:
        print(*res)
