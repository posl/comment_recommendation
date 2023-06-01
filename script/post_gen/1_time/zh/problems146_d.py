Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v, p, c):
    color[c] = True
    ans[v] = c
    for u in g[v]:
        if u == p:
            continue
        nc = 1
        while color[nc]:
            nc += 1
        dfs(u, v, nc)

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

color = [False] * N
ans = [0] * N
dfs(0, -1, 0)

print(max(ans))
for i in range(N-1):
    print(ans[i]+1)

=======
Suggestion 2

def dfs(v, p, c):
    global color
    color[c] += 1
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v, c)

N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

color = [0] * N
dfs(0, -1, 0)

K = max(color)
print(K)
for i in range(N-1):
    print(color[i])

=======
Suggestion 3

def dfs(v, p, c):
    color = 1
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        if color == c:
            color += 1
        ans[G[v][i]] = color
        dfs(G[v][i], v, color)
        color += 1

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
ans = [0] * N
dfs(0, -1, 0)
print(max(ans))
for i in range(N-1):
    print(ans[i+1])

=======
Suggestion 4

def dfs(node, parent, color, color_used):
    color_used[color] = True
    k = 1
    for child in node:
        if child != parent:
            while color_used[k]:
                k += 1
            print(k)
            dfs(node, node.index(child), k, color_used)

n = int(input())
node = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    node[a-1].append(b-1)
    node[b-1].append(a-1)
print(node)
color_used = [False] * (n+1)
print(1)
dfs(node, 0, 1, color_used)

=======
Suggestion 5

def main():
    N = int(input())
    ab = [list(map(int, input().split())) for i in range(N-1)]
    #print(N)
    #print(ab)
    #print(len(ab))
    #print(ab[0])
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1])
    #print(ab[1][0])
    #print(ab[1][1])
    #print(ab[2])
    #print(ab[2][0])
    #print(ab[2][1])
    #print(ab[3])
    #print(ab[3][0])
    #print(ab[3][1])
    #print(ab[4])
    #print(ab[4][0])
    #print(ab[4][1])
    #print(ab[5])
    #print(ab[5][0])
    #print(ab[5][1])
    #print(ab[6])
    #print(ab[6][0])
    #print(ab[6][1])
    #print(ab[7])
    #print(ab[7][0])
    #print(ab[7][1])
    #print(ab[8])
    #print(ab[8][0])
    #print(ab[8][1])
    #print(ab[9])
    #print(ab[9][0])
    #print(ab[9][1])
    #print(ab[10])
    #print(ab[10][0])
    #print(ab[10][1])
    #print(ab[11])
    #print(ab[11][0])
    #print(ab[11][1])
    #print(ab[12])
    #print(ab[12][0])
    #print(ab[12][1])
    #print(ab[13])
    #print(ab[13][0])
    #print(ab[13][1])
    #print(ab[14])
    #print(ab[14][0])
    #print(ab[14][1])
    #print(ab[15])
    #print(ab[15][0])
    #print(ab[15][1])
    #print(ab[16])
    #print(ab[16][0])
    #print(ab[16][1])
    #print(ab[17])
    #print(ab[17][0])
    #print(ab[17][1])
    #print(ab[18

=======
Suggestion 6

def solve():
    pass

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def dfs(v, p, c):
    global color
    color[c] += 1
    for e in G[v]:
        if e == p:
            continue
        dfs(e, v, c)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

color = [0] * N
dfs(0, -1, 0)
print(max(color))
for i in range(N - 1):
    print(color[i + 1])

=======
Suggestion 9

def dfs(v, p, c):
    color[c] = True
    col = 1
    for nv in G[v]:
        if nv == p:
            continue
        while color[col]:
            col += 1
        ans[nv] = col
        dfs(nv, v, col)
        col += 1

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

ans = [0 for _ in range(N)]
color = [False for _ in range(N)]
ans[0] = 1
dfs(0, -1, 1)
print(max(ans))
for c in ans:
    print(c)

=======
Suggestion 10

def dfs(v, p):
    global k
    global color
    c = 1
    for u in g[v]:
        if u == p:
            continue
        if c == color[v]:
            c += 1
        color[u] = c
        k = max(k, c)
        dfs(u, v)
        c += 1

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

color = [-1] * n
color[0] = 1
k = 1
dfs(0, -1)

print(k)
for i in range(n - 1):
    print(color[i + 1])
