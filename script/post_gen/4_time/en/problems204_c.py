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
    print(A)
    print(B)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
    ans = 0
    for i in range(n):
        visited = [False] * n
        stack = [i]
        while stack:
            v = stack.pop()
            if v == i:
                ans += 1
                break
            if not visited[v]:
                visited[v] = True
                stack.extend(graph[v])
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
    ans = 0
    for i in range(N):
        visited = [False] * N
        q = [i]
        visited[i] = True
        while q:
            v = q.pop()
            for u in G[v]:
                if not visited[u]:
                    visited[u] = True
                    q.append(u)
        ans += sum(visited)
    print(ans)

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(1,N+1):
        ans += A.count(i)*B.count(i)
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * (M + 1)
    B = [0] * (M + 1)
    for i in range(1, M + 1):
        A[i], B[i] = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                ans += 1
            else:
                for k in range(1, M + 1):
                    if A[k] == i and B[k] == j:
                        break
                else:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    print(N*(N-1)//2 - M)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    print(N**2 - N - M)

=======
Suggestion 9

def solve():
    N, M = map(int, input().split())
    print(N**2 - N - M)

=======
Suggestion 10

def get_input():
    n, m = map(int, input().split())
    return n, m
