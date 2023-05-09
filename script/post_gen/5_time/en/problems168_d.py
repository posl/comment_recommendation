Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print("Yes")
    for i in range(1, N + 1):
        print(i - 1 if i % 2 == 0 else i + 1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print("Yes")
    for i in range(1, N):
        print(A[B.index(i + 1)] if i + 1 in B else 1)

=======
Suggestion 3

def main():
    N, M = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    print("Yes")
    for i in range(N-1):
        print(A[B.index(i+2)])

=======
Suggestion 4

def main():
    N, M = [int(x) for x in input().split()]
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = [int(x) for x in input().split()]
    #print(N, M, A, B)
    #print('Yes')
    #for i in range(2, N+1):
    #    print(i)

    n = 0
    for i in range(1, N+1):
        n = 0
        for j in range(M):
            if A[j] == i or B[j] == i:
                n += 1
        print(n)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    d = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        d[a].append(b)
        d[b].append(a)
    visited = [False] * n
    visited[0] = True
    q = [0]
    ans = [0] * n
    while q:
        t = q.pop()
        for i in d[t]:
            if visited[i]:
                continue
            visited[i] = True
            ans[i] = t + 1
            q.append(i)
    print("Yes")
    for i in ans[1:]:
        print(i)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a,b = [0] * m, [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    print("Yes")
    for i in range(1,n):
        print(a[b.index(i)] if i in b else b[a.index(i)])

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]

    ans = [0] * n
    for a, b in ab:
        ans[a-1] += 1
        ans[b-1] += 1

    for v in ans:
        if v % 2:
            print('No')
            return

    print('Yes')
    for v in ans:
        print(1)

main()

=======
Suggestion 8

def dfs(v, g, ans):
    for u in g[v]:
        if ans[u] == -1:
            ans[u] = v
            dfs(u, g, ans)

=======
Suggestion 9

def dfs(v, p):
    for i in G[v]:
        if i == p: continue
        if not seen[i]:
            seen[i] = True
            dfs(i, v)
        else:
            print("Yes")
            print(v)
            print(i)
            exit()

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

seen = [False] * (N+1)
seen[1] = True
dfs(1, 0)
print("No")

=======
Suggestion 10

def dfs(v, p):
    global flag
    if visit[v]:
        if visit[v] == 1:
            flag = 0
        return
    visit[v] = 1
    for i in G[v]:
        if i == p:
            continue
        dfs(i, v)
    visit[v] = 2

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)
visit = [0]*N
flag = 1
dfs(0, -1)
