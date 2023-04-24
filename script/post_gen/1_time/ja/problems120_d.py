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
    print(N)
    print(M)
    print(A)
    print(B)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(N - 1)
    for i in range(1, M):
        if A[i] < B[i]:
            print((A[i] - 1) * (N - B[i]))
        else:
            print((B[i] - 1) * (N - A[i]))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # print(N, M)
    # print(A)
    # print(B)
    # print("===")

    # 1. まず、すべての島がつながっていると仮定して、不便さを計算する
    # 2. その後、橋を崩壊させる
    # 3. 橋を崩壊させたときに、どの島がつながっているかを記録しておく
    # 4. 橋を崩壊させることで、島がつながっていない場合は、不便さを増やす
    # 5. すべての橋を崩壊させたら、最終的な不便さを出力する

    # 1. まず、すべての島がつながっていると仮定して、不便さを計算する
    inconvenience = N * (N - 1) // 2

    # 2. その後、橋を崩壊させる
    # 3. 橋を崩壊させたときに、どの島がつながっているかを記録しておく
    # 4. 橋を崩壊させることで、島がつながっていない場合は、不便さを増やす
    # 5. すべての橋を崩壊させたら、最終的な不便さを出力する
    # 2. その後、橋を崩壊させる
    # 3. 橋

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    # 隣接リスト
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        adj[A[i]].append(B[i])
        adj[B[i]].append(A[i])

    # 連結成分ごとに分割
    visited = [False] * (N + 1)
    def dfs(v, cc):
        visited[v] = True
        cc.append(v)
        for next_v in adj[v]:
            if not visited[next_v]:
                dfs(next_v, cc)

    cc_list = []
    for v in range(1, N + 1):
        if not visited[v]:
            cc = []
            dfs(v, cc)
            cc_list.append(cc)

    # 各連結成分について、その中に含まれる頂点の個数から不便さを求める
    ans = 0
    for cc in cc_list:
        n = len(cc)
        ans += n * (n - 1) // 2

    # 橋を渡していた場合は、それぞれの連結成分の頂点の個数の積を不便さから引く
    bridge = [False] * M
    for i in range(M):
        a = A[i]
        b = B[i]
        for cc in cc_list:
            if a in cc and b in cc:
                bridge[i] = True
                break
    for i in range(M):
        if bridge[i]:
            ans -= len(cc_list[i // 2]) * len(cc_list[i // 2 + 1])

    # 橋が崩落する順番に不便さを出力
    ans_list = [ans]
    for i in range(M - 1, 0, -1):
        if bridge[i]:
            ans -= len(cc_list[i // 2]) * len(cc_list[i // 2 + 1])
        ans_list.append(ans)

    for

=======
Suggestion 5

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ans = [0] * m
    ans[-1] = n * (n - 1) // 2
    uf = UnionFind(n)
    for i in range(m - 1, 0, -1):
        a, b = ab[i]
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i - 1] = ans[i]
        else:
            ans[i - 1] = ans[i] - uf.size(a) * uf.size(b)
            uf.union(a, b)
    print(*ans, sep='\n')

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = []
    ans.append(N*(N-1)//2)
    uf = UnionFind(N)
    for i in range(M-1, 0, -1):
        a = AB[i][0]-1
        b = AB[i][1]-1
        if uf.same(a, b):
            ans.append(ans[-1])
        else:
            ans.append(ans[-1] - uf.size(a)*uf.size(b))
            uf.union(a, b)
    for i in range(M-1, -1, -1):
        print(ans[i])

=======
Suggestion 8

def main():
    # 標準入力から値を取得する
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    # 隣接リスト
    G = [[] for _ in range(N+1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)

    # グラフGにおいて、頂点1からの最短距離を求める
    # 計算量はO(N+M)
    from collections import deque
    dist = [-1] * (N+1)
    dist[1] = 0
    que = deque([1])
    while que:
        v = que.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                que.append(nv)

    # 崩落する橋の順番を逆順にして、順番に橋を崩落させる
    # 計算量はO(M)
    ans = []
    for a, b in reversed(AB):
        # 橋(a, b)を崩落させる
        # ただし、aからbへの橋を崩落させたとき、
        # aからの最短距離がbからの最短距離よりも大きい場合は、
        # aからの最短距離をbからの最短距離と同じにする
        if dist[a] == dist[b] + 1:
            ans.append(dist[a] * (N - dist[a]))
        else:
            ans.append(dist[a] * (N - dist[a]))
            dist[a] = dist[b] + 1

    # 崩落する橋の順番を逆順にして出力する
    # 計算量はO(M)
    for a in reversed(ans):
        print(a)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    ab = sorted(ab, key=lambda x: x[1])
    #print(ab)
    ans = 0
    #print(ab[0][1])
    for i in range(M):
        #print(ab[i][0])
        if ab[i][0] < ab[i][1]:
            ans += 1
            #print(ans)
    print(ans)

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    A_B = []
    for i in range(M):
        A_B.append(list(map(int,input().split())))
    print(A_B)
