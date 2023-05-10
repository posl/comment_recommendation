Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N,M = map(int,input().split())
    print(N*M)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    print(N, M)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    ans = 0
    for i in range(m):
        for j in range(m):
            if a[i] == b[j]:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    print(n, m)

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)

    C = []
    for i in range(N):
        c = []
        for j in range(N):
            if i == j:
                c.append(1)
            else:
                c.append(0)
        C.append(c)

    for i in range(M):
        C[A[i]-1][B[i]-1] = 1

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if C[j][i] == 1 and C[i][k] == 1:
                    C[j][k] = 1

    ans = 0
    for i in range(N):
        for j in range(N):
            if C[i][j] == 1:
                ans += 1

    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    print(n, m)
    print(a)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    print(N,M,A,B)

=======
Suggestion 8

def main():
    # 標準入力の取得
    n, m = map(int, input().split())
    # 都市の組み合わせの数を格納する変数
    ans = 0
    # 都市の組み合わせの数を計算
    ans = n * (n - 1) // 2
    # 都市の組み合わせの数を出力
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return

    # 隣接リスト
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)

    # 頂点 0 から各頂点への距離
    dist = [0] * N

    # 幅優先探索
    from collections import deque
    q = deque([0])
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if dist[nv] == 0:
                dist[nv] = dist[v] + 1
                q.append(nv)

    # 頂点 0 から各頂点への距離が 2 以上のものの個数を数える
    print(sum(1 for d in dist if d >= 2))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # print(N, M)
    # print(A)
    # print(B)
    # print('-----')

    # 都市1からスタートして、都市Nにゴールする組み合わせを出す
    # 都市1からスタートして、都市Nにゴールする組み合わせを出す
    # 都市2からスタートして、都市Nにゴールする組み合わせを出す
    # 都市3からスタートして、都市Nにゴールする組み合わせを出す
    # 都市4からスタートして、都市Nにゴールする組み合わせを出す
    # 都市5からスタートして、都市Nにゴールする組み合わせを出す
    # 都市6からスタートして、都市Nにゴールする組み合わせを出す
    # 都市7からスタートして、都市Nにゴールする組み合わせを出す
    # 都市8からスタートして、都市Nにゴールする組み合わせを出す
    # 都市9からスタートして、都市Nにゴールする組み合わせを出す
    # 都市10からスタートして、都市Nにゴールする組み合わせを出す
    # 都市11からスタートして、都市Nにゴールする組み合わせを出す
    # 都市12からスタートして、都市Nにゴールする組み合わせを出す
    # 都市13からスタートして、都市Nにゴールする組み合わせを出す
    #
