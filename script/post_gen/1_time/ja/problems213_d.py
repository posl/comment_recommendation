Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    for i in range(N):
        G[i].sort()
    ans = [0]
    used = [0]*N
    used[0] = 1
    now = 0
    while True:
        for i in G[now]:
            if used[i] == 0:
                ans.append(i+1)
                used[i] = 1
                now = i
                break
        else:
            if now == 0:
                break
            else:
                ans.append(now+1)
                now = ans[-3]
    print(*ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(N-1):
        graph[A[i]-1].append(B[i]-1)
        graph[B[i]-1].append(A[i]-1)
    ans = [1]
    visited = [False] * N
    visited[0] = True
    while len(ans) < N:
        for i in graph[ans[-1]-1]:
            if not visited[i]:
                ans.append(i+1)
                visited[i] = True
                break
        else:
            ans.append(ans[-2])
    print(*ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    print(1, end = " ")
    for i in range(N-1):
        if A[i] == 1:
            print(B[i], end = " ")
            print(1, end = " ")
        elif B[i] == 1:
            print(A[i], end = " ")
            print(1, end = " ")
    print()

=======
Suggestion 4

def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(N)
    #print(A)
    #print(B)

    #道路と都市の関係をグラフで表す
    graph = [[] for _ in range(N)]
    for i in range(N-1):
        graph[A[i]-1].append(B[i]-1)
        graph[B[i]-1].append(A[i]-1)
    #print(graph)

    #旅のルートを記録
    route = [0]
    #訪れた都市を記録
    visited = [0] * N
    #現在いる都市を記録
    now = 0
    #訪れた都市を記録
    visited[now] = 1
    #print(visited)
    #print(route)

    #都市1に戻ってきたら終了
    while now != 0:
        #print("now = ", now)
        #print("route = ", route)
        #print("visited = ", visited)
        #print("graph[now] = ", graph[now])
        #print("visited[graph[now][i]] = ", visited[graph[now][i]])
        #print("visited[graph[now][i]] = ", visited[graph[now][i]])
        #print("route[-1] = ", route[-1])
        #print("graph[route[-1]] = ", graph[route[-1]])
        #print("now = ", now)
        #print("graph[route[-1]] = ", graph[route[-1]])
        #print("visited[graph[route[-1]][i]] = ", visited[graph[route[-1]][i]])
        #print("visited[graph[route[-1]][i]] = ", visited[graph[route[-1]][i]])

        #次にいく都市があれば、次にいく都市へ移動
        #都市1に戻ってきたら終了
        #次にい

=======
Suggestion 5

def main():
    N = int(input())
    A = [0]*(N-1)
    B = [0]*(N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)

=======
Suggestion 6

def main():
    N = int(input())
    roads = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        roads[a-1].append(b-1)
        roads[b-1].append(a-1)

    ans = [0]
    def dfs(before, now):
        for i in roads[now]:
            if i == before:
                continue
            ans.append(i)
            dfs(now, i)
            ans.append(now)
    dfs(0, 0)
    print(' '.join(map(str, [i+1 for i in ans])))

=======
Suggestion 7

def main():
    N = int(input())
    A = [0 for i in range(N)]
    B = [0 for i in range(N)]
    for i in range(N-1):
        a,b = map(int,input().split())
        A[i] = a
        B[i] = b
    #prin

=======
Suggestion 8

def main():
    N = int(input())
    A = [0] * (N+1)
    B = [0] * (N+1)
    for i in range(N-1):
        a,b = map(int,input().split())
        A[a] += 1
        B[b] += 1
    if A.count(1) > 1:
        print(1)
        return
    if B.count(1) > 1:
        print(1)
        return
    for i in range(1,N+1):
        if A[i] == 1:
            print(i)
            return
    for i in range(1,N+1):
        if B[i] == 1:
            print(i)
            return

=======
Suggestion 9

def solve():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    #print(G)
    ans = [0] * N
    ans[0] = 1
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if ans[nv] == 0:
                ans[nv] = v+1
                stack.append(nv)
    print(*ans)
solve()

=======
Suggestion 10

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N-1):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)

    #print(A,B)

    #頂点1からの距離を求める
    dist = [0] * (N+1)
    #print(dist)
    #頂点1からの距離を求める
    def dfs(v, p, d):
        dist[v] = d
        for u in E[v]:
            if u == p:
                continue
            dfs(u, v, d + 1)

    #辺のリスト
    E = [[] for _ in range(N+1)]
    for i in range(N-1):
        E[A[i]].append(B[i])
        E[B[i]].append(A[i])

    #print(E)
    dfs(1, -1, 0)
    #print(dist)

    #頂点1からの距離が奇数の頂点を取得
    odd = []
    for i in range(1,N+1):
        if dist[i]%2 == 1:
            odd.append(i)

    #print(odd)

    if len(odd) <= N//2:
        print(*[1] + odd)
    else:
        print(*[1] + [i for i in range(2,N+1) if i not in odd])
