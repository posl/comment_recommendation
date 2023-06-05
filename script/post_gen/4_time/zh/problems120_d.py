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
    print(N, M)
    print(A)
    print(B)
    return 0

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    for i in range(1, m + 1):
        a[i], b[i] = map(int, input().split())
    ans = [0] * (m + 1)
    uf = UnionFind(n + 1)
    cur = n * (n - 1) // 2
    for i in range(m, 0, -1):
        ans[i] = cur
        if uf.find(a[i]) != uf.find(b[i]):
            cur -= uf.size(a[i]) * uf.size(b[i])
            uf.union(a[i], b[i])
    for i in range(1, m + 1):
        print(ans[i])

=======
Suggestion 3

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

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

def findRoot(root, x):
    if root[x] == x:
        return x
    else:
        root[x] = findRoot(root, root[x])
        return root[x]

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = [0 for _ in range(m)]
    b = [0 for _ in range(m)]
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    print(n,m,a,b)

=======
Suggestion 8

def find_root(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_root(parent[x])
        return parent[x]

=======
Suggestion 9

def readinput():
    n,m = list(map(int,input().split()))
    ab=[]
    for _ in range(m):
        a,b = list(map(int,input().split()))
        ab.append((a,b))
    return n,m,ab

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    # まず、ABをソートする。
    AB.sort(key=lambda x: x[1])

    # ある橋の左側にある島の数を数える
    left_island = [0] * (N + 1)
    for a, b in AB:
        left_island[b] = left_island[a] + 1

    # ある橋の右側にある島の数を数える
    right_island = [0] * (N + 1)
    for a, b in AB[::-1]:
        right_island[a] = right_island[b] + 1

    # ある橋が倒れたときに不便な島の数を数える
    inconvenience = [0] * M
    for i, (a, b) in enumerate(AB):
        inconvenience[i] = left_island[a] * right_island[b]

    # 不便な島の数を出力する
    for i in inconvenience:
        print(i)
