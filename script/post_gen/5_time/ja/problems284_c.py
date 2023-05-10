Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i] == False:
            ans += 1
            visited[i] = True
            stack = [i]
            while len(stack) > 0:
                v = stack.pop()
                for nv in graph[v]:
                    if visited[nv] == False:
                        visited[nv] = True
                        stack.append(nv)
    print(ans)

=======
Suggestion 2

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

seen = [False] * N
ans = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    ans += 1
print(ans)

=======
Suggestion 3

def dfs(v):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

seen = [False] * N
ans = 0
for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    ans += 1
print(ans)

=======
Suggestion 4

def dfs(v):
    seen[v] = True

    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
seen = [False] * N

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

count = 0

for v in range(N):
    if seen[v]:
        continue
    dfs(v)
    count += 1

print(count)

=======
Suggestion 5

def get_parent(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent, parent[x])
        return parent[x]

=======
Suggestion 6

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

seen = [False] * n
count = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
    count += 1

print(count)

=======
Suggestion 7

def dfs(v):
    seen[v] = True
    for i in range(n):
        if G[v][i] == 0:
            continue
        if seen[i]:
            continue
        dfs(i)

n, m = map(int, input().split())
G = [[0] * n for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = 1
    G[b][a] = 1

seen = [False] * n
ans = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)
    ans += 1
print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())

    # 連結成分数を求める
    ans = 0
    # 連結成分数を求める
    ans = 0
    for i in range(M):
        # 辺 i を削除する
        # 連結成分数を求める
        visited = [False] * N
        visited[0] = True
        q = [0]
        while len(q) > 0:
            x = q.pop(0)
            for j in range(M):
                if u[j] == x:
                    if visited[v[j] - 1] == False:
                        visited[v[j] - 1] = True
                        q.append(v[j] - 1)
                if v[j] == x:
                    if visited[u[j] - 1] == False:
                        visited[u[j] - 1] = True
                        q.append(u[j] - 1)

        # 辺 i を追加する
        if visited[u[i] - 1] == False or visited[v[i] - 1] == False:
            ans += 1
        else:
            visited = [False] * N
            visited[0] = True
            q = [0]
            while len(q) > 0:
                x = q.pop(0)
                for j in range(M):
                    if u[j] == x:
                        if visited[v[j] - 1] == False:
                            visited[v[j] - 1] = True
                            q.append(v[j] - 1)
                    if v[j] == x:
                        if visited[u[j] - 1] == False:
                            visited[u[j] - 1] = True
                            q.append(u[j] - 1)
            if visited[u[i] - 1] == False or visited[v[i] - 1] == False:
                ans += 1

    print(ans)

main()

=======
Suggestion 9

def dfs(G, v, seen):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v] == False:
            dfs(G, next_v, seen)
    return seen

=======
Suggestion 10

def dfs(v):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

seen = [False] * n

count = 0
for v in range(n):
    if seen[v]:
        continue
    dfs(v)
    count += 1

print(count)
