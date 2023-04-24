Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0] * N
    ans[0] = -1
    for i in range(M):
        if A[i] == 1:
            ans[B[i] - 1] = 1
        if B[i] == 1:
            ans[A[i] - 1] = 1
    if 0 in ans:
        print("No")
    else:
        print("Yes")
        for i in range(N - 1):
            print(ans[i])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0] * N
    for i in range(M):
        if A[i] == 1:
            ans[B[i]-1] = A[i]
        if B[i] == 1:
            ans[A[i]-1] = B[i]
    for i in range(M):
        if ans[A[i]-1] == 0 and ans[B[i]-1] != 0:
            ans[A[i]-1] = B[i]
        if ans[B[i]-1] == 0 and ans[A[i]-1] != 0:
            ans[B[i]-1] = A[i]
    for i in range(N):
        if ans[i] == 0:
            print("No")
            return
    print("Yes")
    for i in range(N):
        print(ans[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    graph = [[] for i in range(N+1)]
    for i in range(M):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])

    ans = [0] * (N+1)
    ans[1] = -1
    que = [1]
    while que:
        now = que.pop()
        for i in graph[now]:
            if ans[i] == 0:
                ans[i] = now
                que.append(i)

    if 0 in ans[2:]:
        print("No")
    else:
        print("Yes")
        for i in range(2, N+1):
            print(ans[i])

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    # 辺を追加するグラフ
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])
    
    # 部屋 1 からの距離を BFS で計算
    dist = [-1]*(N+1)
    dist[1] = 0
    q = [1]
    while len(q) > 0:
        v = q.pop(0)
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    
    # 部屋 1 からの距離が最も遠い部屋を探す
    max_dist = 0
    max_dist_room = 0
    for i in range(1, N+1):
        if max_dist < dist[i]:
            max_dist = dist[i]
            max_dist_room = i
    
    # 部屋 1 からの距離が最も遠い部屋からの道しるべを辿る
    ans = [0]*(N+1)
    ans[max_dist_room] = 1
    for i in range(max_dist-1, -1, -1):
        for nv in graph[max_dist_room]:
            if dist[nv] == i:
                max_dist_room = nv
                ans[nv] = 1
                break
    
    # 出力
    print('Yes')
    for i in range(1, N+1):
        print(ans[i])

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * (M + 1)
    B = [0] * (M + 1)
    for i in range(1, M + 1):
        A[i], B[i] = map(int, input().split())

    # 部屋1から各部屋への最短距離を求める
    # 部屋1から各部屋への最短距離が偶数のとき、その部屋に道しるべを設置する
    # 部屋1から各部屋への最短距離が奇数のとき、その部屋に道しるべを設置しない
    # 部屋1から各部屋への最短距離が偶数のとき、その部屋から出発して最短距離の部屋に移動する
    # 部屋1から各部屋への最短距離が奇数のとき、その部屋から出発して最短距離の部屋に移動すると、部屋1にたどり着けない
    # 部屋1から各部屋への最短距離が奇数のとき、その部屋から出発して最短距離の部屋に移動すると、部屋1にたどり着けない
    # 部屋1から各部屋への最短距離が偶数のとき、その部屋から出発して最短距離の部屋に移動すると、部屋1にたどり着ける
    # 部屋1から各部屋への最短

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        E[A].append(B)
        E[B].append(A)
    ans = [-1] * N
    ans[0] = 0
    que = [0]
    while que:
        now = que.pop()
        for nxt in E[now]:
            if ans[nxt] == -1:
                ans[nxt] = now
                que.append(nxt)
    if -1 in ans:
        print('No')
    else:
        print('Yes')
        for i in range(1, N):
            print(ans[i] + 1)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]

    for i in range(M):
        A, B = map(int, input().split())
        edge[A - 1].append(B - 1)
        edge[B - 1].append(A - 1)

    print("Yes")
    for i in range(1, N):
        print(edge[i][0] + 1)

main()

上記のコードでWAが出ました。なぜかわかりません。

最初の行を追加してみたらACでした。

import sys
input = sys.stdin.readline

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = [0] * N
    ans[0] = -1
    ans[1] = 1
    for a, b in AB:
        if ans[a-1] == 0:
            ans[a-1] = b
        if ans[b-1] == 0:
            ans[b-1] = a
    if 0 in ans:
        print("No")
    else:
        print("Yes")
        for i in range(1, N):
            print(ans[i])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    if M != N-1:
        print("No")
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = [list(map(lambda x: x-1, a)) for a in AB]
    AB.sort()
    ans = [0]*N
    ans[0] = 1
    for i in range(M):
        if ans[AB[i][0]] == 0:
            ans[AB[i][0]] = AB[i][1]+1
        elif ans[AB[i][1]] == 0:
            ans[AB[i][1]] = AB[i][0]+1
        else:
            print("No")
            return
    print("Yes")
    for i in range(N):
        print(ans[i])

=======
Suggestion 10

def solve(n, m, a, b):
    # 部屋の数だけ、道しるべの先を格納する配列を用意
    ans = [0] * n

    # 部屋の数だけ、部屋に繋がっている道しるべの数を格納する配列を用意
    cnt = [0] * n

    # 部屋の数だけ、部屋に繋がっている道しるべの先を格納する配列を用意
    # 2次元配列にする
    to = [[] for _ in range(n)]

    # 部屋の数だけ、部屋に繋がっている道しるべの先を格納する配列を用意
    # 2次元配列にする
    from_ = [[] for _ in range(n)]

    # 部屋に繋がっている道しるべの数をカウント
    for i in range(m):
        cnt[a[i] - 1] += 1
        cnt[b[i] - 1] += 1

    # 部屋に繋がっている道しるべの先を格納
    for i in range(m):
        to[a[i] - 1].append(b[i] - 1)
        to[b[i] - 1].append(a[i] - 1)

    # 部屋に繋がっている道しるべの先を格納
    for i in range(m):
        from_[b[i] - 1].append(a[i] - 1)
        from_[a[i] - 1].append(b[i] - 1)

    # 部屋に繋がっている道しるべの数が2つでない場合は、Noを出力
    for i in range(n):
        if cnt[i] != 2:
            print('No')
            return

    # 部屋に繋がっている道しる
