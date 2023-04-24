Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    if M != N-1:
        print("No")
        return
    for i in range(N):
        if len(G[i]) != 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    u = []
    v = []
    for i in range(M):
        u_i, v_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
    
    if N - 1 == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    if m != n-1:
        print("No")
        return
    for i in range(m):
        u, v = map(int, input().split())
        if u == 1 or v == 1:
            continue
        else:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M != N-1:
        print("No")
        return
    for i in range(M):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        if u != i+1 or v != i+2:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    if M != N - 1:
        print("No")
        return
    for i in range(M):
        for j in range(i + 1, M):
            if edges[i][0] == edges[j][0] or edges[i][0] == edges[j][1] or edges[i][1] == edges[j][0] or edges[i][1] == edges[j][1]:
                print("No")
                return
    print("Yes")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    edges.sort()
    for i in range(N - 1):
        if edges[i][0] != i + 1 or edges[i][1] != i + 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    if M != N-1:
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    else:
        edge = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, input().split())
            edge[u - 1].append(v - 1)
            edge[v - 1].append(u - 1)
        for i in range(n):
            if len(edge[i]) != 2:
                print("No")
                return
        print("Yes")

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print("")

    #グラフの初期化
    graph = [[] for _ in range(N)]

    #グラフへの入力
    for i in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    #print(graph)

    #グラフの状態を確認
    for i in range(N):
        #print(graph[i])
        if graph[i] == []:
            print("No")
            return

    #パスグラフかどうか
    if N == M:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def check_path_graph(N, M, u, v):
    # ここに処理を書く

    return "Yes"
