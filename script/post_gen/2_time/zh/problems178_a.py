Synthesizing 10/10 solutions

=======
Suggestion 1

def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    friend = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)

    group = [0] * N
    group_id = 1
    for i in range(N):
        if group[i] == 0:
            dfs(friend, group, i, group_id)
            group_id += 1
    print(max(group))

=======
Suggestion 3

def find(x):
  if x == parents[x]:
    return x
  else:
    parents[x] = find(parents[x])
    return parents[x]

=======
Suggestion 4

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 5

def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

=======
Suggestion 6

def init(n):
    global parent
    parent = [i for i in range(n + 1)]

=======
Suggestion 7

def findRoots(n, m, edges):
    roots = [i for i in range(n)]
    for edge in edges:
        roots[edge[1]] = roots[edge[0]]
    return roots

=======
Suggestion 8

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

=======
Suggestion 9

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

=======
Suggestion 10

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
