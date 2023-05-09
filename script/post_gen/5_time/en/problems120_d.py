Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    #print(N, M)
    #print(A)
    #print(B)

    # create a list of lists
    # each element is a list of bridges connected to that island
    # the index of the list is the island number
    # the list of bridges is a list of indices in the A and B lists
    # we use indices instead of the actual bridge numbers to save space
    # the list of bridges is sorted by bridge number
    # we could use a set instead of a list, but we would have to convert it to a list before sorting it
    # we could use a dictionary instead of a list, but we would have to convert it to a list before sorting it
    island_connections = [[] for i in range(N+1)]
    for i in range(M):
        island_connections[A[i]].append(i)
        island_connections[B[i]].append(i)
    #print(island_connections)

    # create a list of bridges
    # each element is a list of islands connected to that bridge
    # the index of the list is the bridge number
    # the list of islands is a list of indices in the A and B lists
    # we use indices instead of the actual island numbers to save space
    # the list of islands is sorted by island number
    # we could use a set instead of a list, but we would have to convert it to a list before sorting it
    # we could use a dictionary instead of a list, but we would have to convert it to a list before sorting it
    bridge_connections = [[] for i in range(M)]
    for i in range(M):
        bridge_connections[i].append(A[i])
        bridge_connections[i].append(B[i])
    #print(bridge_connections)

    # create a list of bridges that have been removed
    # each element is a list of bridges that have been removed
    # the index of the list is the number of bridges that have been removed
    # the list of bridges is a list of indices in the A and B lists
    # we use indices instead of the actual bridge numbers to save space
    # the

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    for i in range(1, m + 1):
        a[i], b[i] = map(int, input().split())
    uf = UnionFind(n + 1)
    ans = [0] * (m + 1)
    ans[m] = n * (n - 1) // 2
    for i in range(m, 0, -1):
        ans[i - 1] = ans[i]
        if uf.same(a[i], b[i]):
            continue
        ans[i - 1] -= uf.size(a[i]) * uf.size(b[i])
        uf.unite(a[i], b[i])
    for i in range(1, m + 1):
        print(ans[i])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().spl

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    ab.reverse()
    uf = UnionFind(n)
    ans = [0]
    for i in range(m-1):
        a = ab[i][0] - 1
        b = ab[i][1] - 1
        if uf.same(a,b):
            ans.append(ans[-1])
        else:
            ans.append(ans[-1] + uf.size(a) * uf.size(b))
            uf.union(a,b)
    ans.reverse()
    for i in range(m):
        print(ans[i])

=======
Suggestion 5

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

=======
Suggestion 6

def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

=======
Suggestion 7

def find_set(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_set(parent[x])
        return parent[x]

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(m)]
    bridges.reverse()

    uf = UnionFind(n)
    ans = [0] * m
    ans[m-1] = (n * (n-1)) // 2

    for i in range(m-1):
        a, b = bridges[i]
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i] = ans[i+1]
        else:
            ans[i] = ans[i+1] - uf.size(a) * uf.size(b)
            uf.unite(a, b)

    print(*ans[::-1], sep="\n")

=======
Suggestion 9

def get_ints(): return map(int, input().strip().split())
