Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    print(a,b)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    #print(n,m)
    #edge = []
    #for i in range(m):
    #    edge.append(list(map(int, input().split())))
    #print(edge)
    print(3**n)

=======
Suggestion 4

def get_color_num(n, m):
    if n == 1:
        return 3
    else:
        return 3 * get_color_num(n - 1, m) - get_color_num(n - 2, m)

=======
Suggestion 5

def dfs(v, color):
    global N
    global M
    global A
    global B
    global ans
    global used

    if v == N:
        ans += 1
        return

    for i in range(3):
        if color == i:
            continue
        for j in range(M):
            if A[j] == v + 1:
                used[B[j] - 1] = True
            if B[j] == v + 1:
                used[A[j] - 1] = True
        for k in range(N):
            if used[k]:
                continue
            dfs(v + 1, k)
        for j in range(M):
            if A[j] == v + 1:
                used[B[j] - 1] = False
            if B[j] == v + 1:
                used[A[j] - 1] = False

N, M = map(int, input().split())
A = []
B = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
ans = 0
used = [False] * N
dfs(0, 0)
print(ans)

=======
Suggestion 6

def dfs(v, c):
    color[v] = c
    for i in range(len(edges[v])):
        if color[edges[v][i]] == c:
            return False
        if color[edges[v][i]] == 0 and (not dfs(edges[v][i], -c)):
            return False
    return True

n, m = map(int, input().split())
edges = [[] for i in range(n)]
color = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(i, 1):
            ans += 1
        else:
            print(0)
            exit()

print(3 ** ans)

=======
Suggestion 7

def dfs(n, m, e, v, i):
    if i == n:
        return 1
    res = 0
    for c in range(3):
        ok = True
        for j in range(i):
            if e[i][j] == 1 and v[j] == c:
                ok = False
                break
        if ok:
            v[i] = c
            res += dfs(n, m, e, v, i + 1)
            v[i] = -1
    return res

=======
Suggestion 8

def dfs(v, c):
    global ans
    color[v] = c
    if v == N - 1:
        ans += 1
        return
    for i in range(N):
        if G[v][i] == 1 and color[i] == -1:
            dfs(i, 0)
            dfs(i, 1)
            dfs(i, 2)
            break

N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1][b - 1] = 1
    G[b - 1][a - 1] = 1

color = [-1] * N
ans = 0
dfs(0, 0)
dfs(0, 1)
dfs(0, 2)
print(ans)

=======
Suggestion 9

def main():
    return
