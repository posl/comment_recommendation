Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    bridge = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        bridge[a] += 1
        bridge[b] += 1
    print(bridge.count(0))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    bridge = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        bridge[a] += 1
        bridge[b] += 1
    print(max(bridge))

=======
Suggestion 3

def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    E = [[] for _ in range(N)]
    for i in range(M):
        E[A[i]].append(B[i])
        E[B[i]].append(A[i])
    #print(E)
    #print(A)
    #print(B)
    #print(N, M)

    # 深さ優先探索
    def dfs(v):
        #print("v", v)
        #print("visited", visited)
        #print("group", group)
        visited[v] = True
        group[v] = g
        for u in E[v]:
            if not visited[u]:
                dfs(u)

    # 連結成分分解
    visited = [False] * N
    group = [-1] * N
    g = 0
    for v in range(N):
        if not visited[v]:
            dfs(v)
            g += 1
    #print("visited", visited)
    #print("group", group)
    #print("g", g)

    # 連結成分の頂点数
    count = [0] * g
    for i in range(N):
        count[group[i]] += 1
    #print("count", count)

    # 連結成分の橋数
    bridge = [0] * g
    for i in range(M):
        if group[A[i]] != group[B[i]]:
            bridge[group[A[i]]] += 1
            bridge[group[B[i]]] += 1
    #print("bridge", bridge)

    # 連結成分の橋数が 0 の数
    zero = 0
    for i in range(g):
        if bridge[i] == 0:
            zero += 1
    #print("zero", zero)

    # 答え
    ans = max(0, zero - 1)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    bridge = [0] * M
    for i in range(M):
        bridge[i] = list(map(int, input().split()))
    bridge.sort(key=lambda x: x[1])

    cnt = 0
    while len(bridge) > 0:
        cnt += 1
        bridge = [x for x in bridge if x[0] < bridge[0][1] and x[1] > bridge[0][1]]

    print(cnt)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))
    edges.sort()
    #print(edges)
    #edges = [(1, 4), (2, 5)]
    #print(edges[0][0])
    #print(edges[0][1])
    #print(edges[1][0])
    #print(edges[1][1])
    #print(edges[1][0] - edges[0][1])
    #print(edges[1][0] - edges[0][1] - 1)
    #print(edges[0][1] - edges[0][0])
    #print(edges[1][1] - edges[1][0])
    ans = 0
    for i in range(M):
        if i == 0:
            ans += edges[0][1] - edges[0][0]
        else:
            ans += edges[i][1] - edges[i][0] - (edges[i][0] - edges[i-1][1] - 1)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    #print(AB)
    cnt = 0
    i = 0
    while i < M:
        cnt += 1
        j = i
        while j < M and AB[j][0] <= AB[i][1]:
            j += 1
        i = j
    print(cnt)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]
    ab = sorted(ab, key=lambda x: (x[0], -x[1]))
    #print(ab)
    ans = 0
    for i in range(M):
        a = ab[i][0]
        b = ab[i][1]
        for j in range(i+1, M):
            if ab[j][0] <= a and b <= ab[j][1]:
                ans += 1
                break
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(M)]
    A.sort(key=lambda x: x[1])
    ans = 0
    tmp = 0
    for a, b in A:
        if tmp < a:
            ans += 1
            tmp = b - 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    bridges.sort()
    print(bridges)
    print(M - N + 1)

=======
Suggestion 10

def solve():
    # 構築
    N, M = map(int, input().split())
    bridge = [list(map(int, input().split())) for _ in range(M)]

    # 連結成分の個数をカウント
    # 連結成分の個数が1になるまで橋を取り除く
    # 連結成分の個数が1になったら終了
    # 連結成分の個数を出力

    # Union-Find
    # https://atcoder.jp/contests/abc167/submissions/12989162
    # https://atcoder.jp/contests/abc167/submissions/12989189
    # https://atcoder.jp/contests/abc167/submissions/12989205
    # https://atcoder.jp/contests/abc167/submissions/12989225
    # https://atcoder.jp/contests/abc167/submissions/12989242
    # https://atcoder.jp/contests/abc167/submissions/12989262
    # https://atcoder.jp/contests/abc167/submissions/12989284
    # https://atcoder.jp/contests/abc167/submissions/12989302
    # https://atcoder.jp/contests/abc167/submissions/12989326
    # https://atcoder.jp/contests/abc167/submissions/12989347
    # https://atcoder.jp/contests/abc167/submissions/12989362
    # https://atcoder.jp/contests/abc167/submissions/12989381
    # https://atcoder.jp/contests/abc167/submissions/12989396
    # https://atcoder.jp/contests/abc167/submissions/12989411
    # https://atcoder.jp/contests/abc167/submissions/12989429
    # https://atcoder.jp/contests/abc167/submissions/12989447
    # https://atcoder.jp/contests/abc167/submissions/12989467
    # https://atcoder.jp/contests/abc167/submissions/12989488
    # https://atcoder.jp/contests
