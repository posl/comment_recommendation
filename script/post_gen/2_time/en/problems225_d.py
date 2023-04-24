Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 2

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 3

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]

=======
Suggestion 4

def find_root(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_root(par[x])
        return par[x]

=======
Suggestion 5

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    trains = [i for i in range(N+1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            trains[query[1]], trains[query[2]] = trains[query[2]], trains[query[1]]
        elif query[0] == 2:
            trains[query[1]], trains[query[2]] = trains[query[2]], trains[query[1]]
        elif query[0] == 3:
            train = query[1]
            while trains[train] != train:
                print(train, end=' ')
                train = trains[train]
            print(train, end=' ')
            print()
    return

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    par = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    def same(x, y):
        return find(x) == find(y)
    for i in range(Q):
        l = list(map(int, input().split()))
        if l[0] == 1:
            unite(l[1], l[2])
        elif l[0] == 2:
            unite(l[1], l[2])
        else:
            ans = []
            for j in range(1, N + 1):
                if same(l[1], j):
                    ans.append(j)
            print(*ans)

=======
Suggestion 8

def parent(x):
    if par[x] == x:
        return x
    else:
        par[x] = parent(par[x])
        return par[x]

=======
Suggestion 9

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])
