Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    for i in range(1, n):
        a[i], b[i] = map(int, input().split())

    ans = n * (n - 1) // 2
    par = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

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

    for i in range(1, n):
        unite(a[i], b[i])

    for i in range(m):
        a, b = map(int, input().split())
        if same(a, b):
            ans -= 1
    print(ans)

=======
Suggestion 2

def findRoot(x, root):
    if x == root[x]:
        return x
    else:
        root[x] = findRoot(root[x], root)
        return root[x]

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0 for i in range(m)]
    b = [0 for i in range(m)]
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    ans = 0
    for i in range(m):
        if i == 0:
            ans = a[0] - 1
        else:
            ans += a[i] - a[i-1] - 1
        if i == m - 1:
            ans += n - b[-1]
    print(ans)

=======
Suggestion 4

def get_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent[x])
        return parent[x]

=======
Suggestion 5

def find_root(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_root(par[x])
        return par[x]

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(M)]
    A.sort(key=lambda x: x[1])
    ans = 0
    bridge = 0
    for i in range(M):
        if A[i][0] > bridge:
            bridge = A[i][1] - 1
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i],b[i] = map(int,input().split())
    #print(a)
    #print(b)
    #print(N)
    #print(M)
    #print(a)
    #print(b)
    #print(N)
    #print(M)
    
    print(N-1-M)
    return 0

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i], b[i] = map(int, input().split())
    #print(a)
    #print(b)
    #print(N)
    #print(M)
    #print(N-1)
    ans = 0
    for i in range(M):
        if a[i] == 1 or b[i] == 1:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    # print(n, m)
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    # print(ab)
    ab.sort(key=lambda x: (x[0], x[1]))
    # print(ab)
    num = 0
    for i in range(m):
        if ab[i][1] <= ab[i+1][0]:
            num += 1
            continue
        else:
            ab[i+1][0] = ab[i][0]
            ab[i+1][1] = min(ab[i][1], ab[i+1][1])
    # print(ab)
    print(num)

=======
Suggestion 10

def root(x):
    if par[x]==x:
        return x
    else:
        par[x]=root(par[x])
        return par[x]
