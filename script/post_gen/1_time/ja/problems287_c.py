Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    e = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        e[u-1].append(v-1)
        e[v-1].append(u-1)
    if M != N - 1:
        print('No')
        return
    for i in range(N):
        if len(e[i]) != 2:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    #入力
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())

    #処理
    #グラフの隣接リストを作成
    graph = [[] for i in range(N)]
    for i in range(M):
        graph[u[i] - 1].append(v[i] - 1)
        graph[v[i] - 1].append(u[i] - 1)
    #print(graph)

    #2頂点を選んで、その間の距離が1以外の辺が存在する場合はNoとする
    for i in range(N):
        for j in range(i + 2, N):
            #print(i, j)
            if j - i == 1:
                continue
            #print(i, j, graph[i], graph[j])
            if j in graph[i]:
                print("No")
                return

    print("Yes")
    return

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if N == M + 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    else:
        for i in range(M):
            u, v = map(int, input().split())
            if u == 1 or v == 1:
                pass
            else:
                print("No")
                return
        print("Yes")
        return

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M != N-1:
        print("No")
        return
    else:
        for i in range(M):
            u, v = map(int, input().split())
            if abs(u-v) != 1:
                print("No")
                return
        print("Yes")
        return

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    else:
        for i in range(m):
            u, v = map(int, input().split())
            if abs(u - v) != 1:
                print("No")
                return
        print("Yes")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    else:
        u = [0] * M
        v = [0] * M
        for i in range(M):
            u[i], v[i] = map(int, input().split())
        if len(set(u)) == len(set(v)) == N:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    if M == 0:
        print('No')
        return
    if M != N - 1:
        print('No')
        return
    edge = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        edge[u-1].add(v-1)
        edge[v-1].add(u-1)
    for i in range(N):
        if len(edge[i]) != 2:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    #各頂点の次数を格納するリスト
    degree = [0] * (N + 1)
    #各頂点の次数を更新
    for _ in range(M):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1
    #各頂点の次数が2であるかチェック
    for i in range(1, N + 1):
        if degree[i] != 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    #入力
    N, M = map(int, input().split())
    #u, vを格納する配列
    u = [0] * M
    v = [0] * M
    #u, vを格納
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    
    #頂点がN個あるので、N個の配列を用意する
    #1, 2, ..., N の番号が付いている
    #各頂点の次数を格納する配列
    deg = [0] * N
    for i in range(M):
        #辺の始点と終点を格納
        #辺の始点はu[i] - 1
        #辺の終点はv[i] - 1
        #u[i]とv[i]の次数をそれぞれ1増やす
        deg[u[i] - 1] += 1
        deg[v[i] - 1] += 1
    
    #パスグラフなら、次数が2でない頂点が存在しない
    #次数が2でない頂点が存在するならNo
    #存在しないならYes
    for i in range(N):
        if deg[i] != 2:
            print("No")
            return
    
    #全ての頂点の次数が2ならYes
    print("Yes")
