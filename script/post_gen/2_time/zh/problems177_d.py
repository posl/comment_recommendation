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
    for i in range(m):
        a.append(list(map(int,input().split())))

    print(n-m)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    friend = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)
    group = [-1]*n
    group[0] = 0
    stack = [0]
    while stack:
        i = stack.pop()
        for j in friend[i]:
            if group[j] == -1:
                group[j] = 1-group[i]
                stack.append(j)
            elif group[j] == group[i]:
                print(0)
                return
    print(group.count(0)*group.count(1)-m)
    return

=======
Suggestion 4

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

=======
Suggestion 5

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 6

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

=======
Suggestion 7

def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == c:
            return False
        if color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True

=======
Suggestion 8

def find_parent(parent,x):
	if parent[x] != x:
		parent[x] = find_parent(parent,parent[x])
	return parent[x]
