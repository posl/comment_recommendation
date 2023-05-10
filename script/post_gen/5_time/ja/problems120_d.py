Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = [0] * M
    ans[M - 1] = N * (N - 1) // 2
    uf = UnionFind(N)
    for i in range(M - 1, 0, -1):
        a = AB[i][0] - 1
        b = AB[i][1] - 1
        if uf.same(a, b):
            ans[i - 1] = ans[i]
        else:
            ans[i - 1] = ans[i] - uf.size(a) * uf.size(b)
            uf.union(a, b)
    for i in range(M):
        print(ans[i])

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    # 1 から N までの連結成分を管理する。
    # 連結成分の個数は N 以下である。
    uf = UnionFind(N)
    # 1 から N までの連結成分の個数を管理する。
    # 連結成分の個数は N 以下である。
    cnt = [1] * N
    # 1 から N までの連結成分の個数の最大値を管理する。
    # 連結成分の個数の最大値は N 以下である。
    ans = N * (N - 1) // 2
    # 1 から N までの連結成分の個数の最大値の履歴を管理する。
    # 連結成分の個数の最大値の履歴は M 以下である。
    ans_history = [ans]

    for i in range(M - 1, 0, -1):
        # 1 から N までの連結成分の個数の最大値の履歴を更新する。
        if ans_history[-1] == 0:
            ans_history.append(0)
        else:
            ans_history.append(ans_history[-1])
        # A[i] と B[i] の連結成分を統合する。
        if uf.same(A[i] - 1, B[i] - 1):
            continue
        ans -= cnt[uf.root(A[i] - 1)] * cnt[uf.root(B[i] - 1)]
        uf.unite(A[i] - 1, B[i] - 1)
        cnt[uf.root(A[i] - 1)] += cnt[uf.root(B[i] - 1)]
        # 1 から N までの連結成

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    
    #print(N, M)
    #print(A)
    #print(B)
    
    # 橋が崩落する前の島の組み合わせ
    # 1 から N 番目の島の組み合わせは、(N-1)*N/2
    # 1 から N-1 番目の島の組み合わせは、(N-2)*(N-1)/2
    # 1 から N-2 番目の島の組み合わせは、(N-3)*(N-2)/2
    # 1 から 1 番目の島の組み合わせは、0
    # 結果は、(N-1)*N/2 + (N-2)*(N-1)/2 + (N-3)*(N-2)/2 + ... + 0
    #       = (N-1)*N/2 + (N-2)*(N-1)/2 + (N-3)*(N-2)/2 + ... + 1*0/2 + 0
    #       = (N-1)*N/2 + (N-2)*(N-1)/2 + (N-3)*(N-2)/2 + ... + 1*0/2
    #       = (N-1)*N/2 + (N-2)*(N-1)/2 + (N-3)*(N-2)/2 + ... + 1*0/2
    #       = (N-1)*N/2 + (N-2)*(N-1)/2 + (N-3)*(N-2)/2 + ... + 1*0/2
    #       = (N-1)*N/2 + (N-2)*(N-1)/2 + (N-3)*(N-2)/2 + ... + 1*0/2

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(M)]
    bridge = [0 for _ in range(N)]
    bridge[0] = N*(N-1)//2
    for i in range(1,N):
        bridge[i] = bridge[i-1] - i
    ans = []
    for i in range(M-1,-1,-1):
        ans.append(bridge[data[i][0]-1]+bridge[data[i][1]-1])
        bridge[data[i][0]-1] -= 1
        bridge[data[i][1]-1] -= 1
    for i in range(M-1,-1,-1):
        print(ans[i])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    #print(N, M)
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
        #print(A[i], B[i])
    #print(A)
    #print(B)
    #print("")

    # 1回目の橋崩落時の不便さを求める
    # 2回目以降は、崩落した橋の両端の島の組み合わせ数を引いて、
    # さらに、崩落した橋の両端の島の組み合わせ数を足すことで求める
    # このようにして、崩落した橋の両端の島の組み合わせ数を2回足し引きすることで、
    # 崩落した橋の両端の島の組み合わせ数を求めることができる
    # このようにして、崩落した橋の両端の島の組み合わせ数を2回足し引きすることで、
    # 崩落した橋の両端の島の組み合わせ数を求めることができる
    # このようにして、崩落した橋の両端の島の組み合わせ数を2回足し引きすることで、
    # 崩落した橋の両端の島の組み合わせ数を求めることができる
    # このようにして、崩落した橋の両端の島の組み合わせ数を2回足し引きすることで

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    ans = [0] * M
    ans[M-1] = N * (N - 1) // 2
    for i in range(M-1, 0, -1):
        if (A[i] < B[i]):
            ans[i-1] = ans[i] - (N - B[i]) * A[i]
            N -= 1
        else:
            ans[i-1] = ans[i] - (N - A[i]) * B[i]
            N -= 1
    for i in range(M):
        print(ans[i])

=======
Suggestion 7

def main():
    # 標準入力受け取り
    input_line = input()
    N, M = map(int, input_line.split())
    #print(N, M)
    input_line = input()
    A, B = map(int, input_line.split())
    #print(A, B)
    # 入力を配列に格納
    A_list = []
    B_list = []
    A_list.append(A)
    B_list.append(B)
    for i in range(1, M):
        input_line = input()
        A, B = map(int, input_line.split())
        #print(A, B)
        A_list.append(A)
        B_list.append(B)
    #print(A_list)
    #print(B_list)
    # 各橋を渡っている島の組み合わせを配列に格納
    bridge_list = []
    for i in range(M):
        bridge_list.append([A_list[i],B_list[i]])
    #print(bridge_list)
    # 2つの島の組み合わせを配列に格納
    island_list = []
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            island_list.append([i,j])
    #print(island_list)
    # 2つの島の組み合わせの組み合わせを配列に格納
    combination_list = []
    for i in range(len(island_list)):
        for j in range(i+1, len(island_list)):
            combination_list.append([island_list[i],island_list[j]])
    #print(combination_list)
    # 2つの島の組み合わせの組み合わせの組み合わせを配列に格納
    combination_list2 = []
    for i in range(len(combination_list)):
        for j in range(i+1, len(combination_list)):
            combination_list2.append([combination_list[i],combination_list[j]])
    #print(combination_list2)
    # 2つの島の組み合わせの組み合わせの組み合わせの組み合

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(N, M)
    # print(A)
    # print(B)
    # print('-------------')

    # 頂点番号を1から始めるために、各要素を-1する
    A = list(map(lambda x: x-1, A))
    B = list(map(lambda x: x-1, B))
    # print(A)
    # print(B)
    # print('-------------')

    # 隣接リスト
    adj = [[] for _ in range(N)]
    for i in range(M):
        adj[A[i]].append(B[i])
        adj[B[i]].append(A[i])
    # print(adj)
    # print('-------------')

    # 頂点1からの距離
    dist = [-1] * N
    # 頂点1からの距離を0にする
    dist[0] = 0
    # 幅優先探索
    queue = [0]
    while len(queue) > 0:
        # 先頭の頂点を取り出す
        v = queue.pop(0)
        # vから行ける頂点を探索
        for u in adj[v]:
            # 未訪問の場合
            if dist[u] == -1:
                # 頂点uへの距離を更新
                dist[u] = dist[v] + 1
                # キューに追加
                queue.append(u)
    # print(dist)
    # print('-------------')

    # 頂点1からの距離が偶数の頂点の数
    n1 = 0
    # 頂点1からの距離が奇数の頂点の数
    n2 = 0
    for i in range(N):
        if dist[i] % 2 == 0:
            n1 += 1
        else:
            n2 += 1
    # print

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    ans = [0]*M
    ans[M-1] = N*(N-1)//2
    uf = UnionFind(N+1)
    for i in range(M-1,0,-1):
        a = AB[i][0]
        b = AB[i][1]
        if uf.same(a,b):
            ans[i-1] = ans[i]
        else:
            ans[i-1] = ans[i] - uf.size(a)*uf.size(b)
            uf.union(a,b)
    for i in range(M):
        print(ans[i])

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a_list = []
    b_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    a_list.reverse()
    b_list.reverse()
    ans = (n-1)*n//2
    ans_list = []
    for i in range(m):
        ans_list.append(ans)
        if a_list[i] > b_list[i]:
            a_list[i], b_list[i] = b_list[i], a_list[i]
        if a_list[i] == 1:
            ans -= n - b_list[i]
        elif b_list[i] == n:
            ans -= a_list[i] - 1
        else:
            ans -= a_list[i] - 1
            ans -= n - b_list[i]
    ans_list.reverse()
    for i in range(m):
        print(ans_list[i])
