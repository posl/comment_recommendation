Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    for i in range(m):
        b.append(list(map(int,input().split())))

    a.sort()
    b.sort()

    if a == b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    c = [list(map(int, input().split())) for _ in range(m)]
    for i in range(m):
        a[i][0] -= 1
        a[i][1] -= 1
        c[i][0] -= 1
        c[i][1] -= 1
    ans = 0
    for i in range(1 << n):
        ok = True
        for j in range(m):
            if ((i >> a[j][0]) & 1) ^ ((i >> a[j][1]) & 1):
                ok = False
        if not ok:
            continue
        now = 0
        for j in range(n):
            if (i >> j) & 1:
                now += 1 << j
        for j in range(m):
            if ((now >> c[j][0]) & 1) ^ ((now >> c[j][1]) & 1):
                ok = False
        if ok:
            ans += 1
    if ans == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M

    for i in range(M):
        A[i], B[i] = map(int, input().split())

    for i in range(M):
        C[i], D[i] = map(int, input().split())

    for i in range(M):
        A[i] -= 1
        B[i] -= 1
        C[i] -= 1
        D[i] -= 1

    def calc(state):
        res = 0
        for i in range(M):
            if (state >> A[i]) & 1 and (state >> B[i]) & 1:
                res |= 1 << i
            if (state >> C[i]) & 1 and (state >> D[i]) & 1:
                res |= 1 << i
        return res

    ok = True
    for state in range(1 << N):
        if bin(state).count('1') != N // 2:
            continue
        if calc(state) == (1 << M) - 1:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def check(n, m, a, b, c, d, p):
    for i in range(m):
        if ((p[a[i]-1] < p[b[i]-1]) != (c[i]-1 < d[i]-1)):
            return False
    return True

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def check(perm, a, b):
    for i in range(len(a)):
        if perm[a[i]-1] > perm[b[i]-1]:
            return False
    return True

n, m = map(int, input().split())
a = []
b = []
for i in range(m):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
c = []
d = []
for i in range(m):
    x, y = map(int, input().split())
    c.append(x)
    d.append(y)

p = [i for i in range(1, n+1)]
ans = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        p[i-1], p[j-1] = p[j-1], p[i-1]
        if check(p, a, b) and check(p, c, d):
            ans += 1
        p[i-1], p[j-1] = p[j-1], p[i-1]

=======
Suggestion 7

def permutation(n, m, a, b, c, d):
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                for l in range(1,n+1):
                    if i==j or i==k or i==l or j==k or j==l or k==l:
                        continue
                    if (a[i] < a[j] and b[i] < b[j]) == (c[k] < c[l] and d[k] < d[l]):
                        continue
                    if (a[i] < a[j] and b[i] < b[j]) != (c[k] < c[l] and d[k] < d[l]):
                        return False
    return True

=======
Suggestion 8

def dfs(i, v, g, visited):
    visited[i] = v
    for j in g[i]:
        if visited[j] == -1:
            dfs(j, v, g, visited)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
visited1 = [-1] * n
visited2 = [-1] * n
dfs(0, 0, g, visited1)
dfs(0, 1, g, visited2)
print("Yes" if visited1 == visited2 else "No")

=======
Suggestion 9

def main():
    n,m=map(int,input().split())
    a=[]
    b=[]
    c=[]
    d=[]
    for i in range(m):
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(m):
        x,y=map(int,input().split())
        c.append(x)
        d.append(y)
    for i in range(m):
        if a[i] in c and b[i] in d:
            continue
        elif a[i] in d and b[i] in c:
            continue
        else:
            print("No")
            break
    else:
        print("Yes")
