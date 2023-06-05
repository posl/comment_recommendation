Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def dfs(v,c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and dfs(G[v][i],-c) == False:
            return False
    return True

N,M = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

color = [0]*N
ans = 1
for i in range(N):
    if color[i] == 0:
        if dfs(i,1) == False:
            ans = 0
            break
print(ans*3**color.count(0))

=======
Suggestion 2

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c: return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c): return False
    return True

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
color = [0] * N
ans = 0
for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            ans = 0
            break
        else:
            ans += 1
print(ans)

=======
Suggestion 3

def solve(n, m, edges):
    colors = ['R', 'G', 'B']
    def dfs(i, color):
        colors[i] = color
        for j in edges[i]:
            if colors[j] == color:
                return False
            if colors[j] == None and not dfs(j, 'R' if color == 'G' else 'G'):
                return False
        return True

    res = 0
    for i in range(n):
        colors = [None] * n
        if dfs(i, 'R'):
            res += 1
        colors = [None] * n
        if dfs(i, 'G'):
            res += 1
        colors = [None] * n
        if dfs(i, 'B'):
            res += 1
    return res

=======
Suggestion 4

def dfs(u, c):
    color[u] = c
    for i in range(N):
        if G[u][i] == 0:
            continue
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True

N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]
color = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = G[b - 1][a - 1] = 1

=======
Suggestion 5

def dfs(i, c):
    global G, N, M
    color[i] = c
    for j in range(len(G[i])):
        if color[G[i][j]] == c:
            return False
        if color[G[i][j]] == 0 and not dfs(G[i][j], -c):
            return False
    return True

N, M = map(int, input().split())
G = [[] for i in range(N)]
color = [0 for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

ans = 1
for i in range(N):
    if color[i] == 0:
        if not dfs(i, 1):
            ans = 0
            break
print(ans * 3 ** sum(c == 0 for c in color))

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    edge = [list(map(int,input().split())) for _ in range(m)]
    print(edge)
    print(n,m)
    print(edge[0][0])

=======
Suggestion 8

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and dfs(G[v][i], -c) == False:
            return False
    return True

N, M = map(int, input().split())
G = [[] for i in range(N)]
color = [0 for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

ans = 1
for i in range(N):
    if color[i] == 0:
        if dfs(i, 1):
            ans *= 3
        else:
            ans = 0

print(ans)

=======
Suggestion 9

def dfs(v, c):
    color[v] = c
    for i in range(0, len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and dfs(G[v][i], -c) == False:
            return False
    return True

N, M = map(int, input().split())
G = [[] for i in range(0, N)]
color = [0 for i in range(0, N)]

for i in range(0, M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = 1
for i in range(0, N):
    if color[i] == 0:
        if dfs(i, 1) == False:
            ans = 0
            break

print(ans * 3 ** color.count(0))
