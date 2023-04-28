Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.reverse()
    B.reverse()
    ans = N * (N - 1) // 2
    uf = UnionFind(N)
    anss = []
    for i in range(M):
        anss.append(ans)
        a = A.pop()
        b = B.pop()
        if uf.same(a - 1, b - 1):
            continue
        ans -= uf.size(a - 1) * uf.size(b - 1)
        uf.unite(a - 1, b - 1)
    anss.reverse()
    for i in range(M):
        print(anss[i])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    ans = 0
    ans_list = [0] * M
    ans_list[M-1] = int(N*(N-1)/2)
    for i in range(M-1, 0, -1):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
        if A[i] == 1:
            ans_list[i-1] = ans_list[i] - (N - B[i])*(N - B[i] - 1)/2
        else:
            ans_list[i-1] = ans_list[i] - (N - B[i])*(N - B[i] - 1)/2 + (A[i] - 1)*(A[i] - 2)/2
    for i in range(M):
        print(int(ans_list[i]))

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    ans = [0]*m
    ans[-1] = n*(n-1)//2
    uf = UnionFind(n+1)
    for i in range(m-1,0,-1):
        ans[i-1] = ans[i]
        if uf.root(a[i]) != uf.root(b[i]):
            ans[i-1] -= uf.size(a[i])*uf.size(b[i])
            uf.unite(a[i],b[i])
    print(*ans,sep="\n")

=======
Suggestion 4

def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]

    uf = UnionFind(n)
    ans = [0] * m
    ans[m-1] = n * (n - 1) // 2

    for i in range(m-1, 0, -1):
        a, b = ab[i]
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i-1] = ans[i]
        else:
            ans[i-1] = ans[i] - uf.size(a) * uf.size(b)
        uf.union(a, b)

    for i in range(m):
        print(ans[i])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])

    uf = UnionFind(N)
    ans = [0]
    for a, b in AB:
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans.append(ans[-1])
        else:
            ans.append(ans[-1] + uf.size(a) * uf.size(b))
            uf.union(a, b)
    ans.pop(0)
    ans.reverse()
    print(*ans, sep='\n')

=======
Suggestion 7

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab = ab[::-1]
    uf = UnionFind(n)
    ans = [0] * m
    ans[0] = n * (n - 1) // 2
    for i in range(m - 1):
        a, b = ab[i + 1]
        ans[i + 1] = ans[i]
        if uf.same(a - 1, b - 1):
            continue
        ans[i + 1] -= uf.size(a - 1) * uf.size(b - 1)
        uf.union(a - 1, b - 1)
    print(*ans[::-1], sep="\n")

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    uf = UnionFind(n)
    ans = [0] * m
    ans[-1] = n * (n - 1) // 2

    for i in range(m - 1, 0, -1):
        a, b = edges[i]
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i - 1] = ans[i]
        else:
            ans[i - 1] = ans[i] - uf.size(a) * uf.size(b)
            uf.merge(a, b)

    print(*ans, sep='\n')

=======
Suggestion 10

def main():
    n,m = map(int, input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    ab.reverse()
    ans = [0]*m
    uf = UnionFind(n)
    ans[0] = n*(n-1)//2
    for i in range(m-1):
        a = ab[i][0]-1
        b = ab[i][1]-1
        if uf.same(a,b):
            ans[i+1] = ans[i]
        else:
            ans[i+1] = ans[i]-uf.size(a)*uf.size(b)
            uf.union(a,b)
    ans.reverse()
    for i in ans:
        print(i)
