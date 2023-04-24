Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    u = [0]*M
    v = [0]*M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    if N == M:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    path = [0] * N
    for i in range(M):
        path[A[i] - 1] += 1
        path[B[i] - 1] += 1
    if max(path) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    edges = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        edges[u-1].add(v-1)
        edges[v-1].add(u-1)
    if m != n - 1:
        print("No")
        return
    for i in range(n):
        if len(edges[i]) != 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort()
    for i in range(M):
        if edges[i][0] != i + 1 or edges[i][1] != i + 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    edges = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].add(v)
        edges[v].add(u)
    for i in range(N):
        if len(edges[i]) != 2:
            print('No')
            return
    print('Yes')

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    else:
        for _ in range(M):
            u, v = map(int, input().split())
            if abs(u - v) != 1:
                print("No")
                return
        print("Yes")
        return

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    if n == m:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    if M == 0:
        print('Yes')
        return
    if M != N - 1:
        print('No')
        return
    nodes = [0] * (N + 1)
    for u, v in edges:
        nodes[u] += 1
        nodes[v] += 1
    print('Yes' if all(n == 2 for n in nodes) else 'No')

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    else:
        print("Yes")
        return

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print('No')
        return
    parent = list(range(n))
    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]
    def union(i, j):
        parent[find(i)] = find(j)
    for _ in range(m):
        i, j = map(int, input().split())
        union(i - 1, j - 1)
    print('Yes' if len(set(find(i) for i in range(n))) == 1 else 'No')
