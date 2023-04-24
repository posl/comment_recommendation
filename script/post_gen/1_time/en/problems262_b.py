Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    ans = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) in edges:
                for k in range(j + 1, n + 1):
                    if (j, k) in edges and (k, i) in edges:
                        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    matrix = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        matrix[a-1][b-1] = 1
        matrix[b-1][a-1] = 1
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[k][i] == 1:
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    g = [[0] * n for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        g[a-1][b-1] = 1
        g[b-1][a-1] = 1
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if g[i][j] == 1 and g[i][k] == 1 and g[j][k] == 1:
                    ans += 1
    print(ans)
main()

=======
Suggestion 4

def solve(N, M, U, V):
    ans = 0
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            for c in range(b + 1, N + 1):
                if (a, b) in zip(U, V) and (b, c) in zip(U, V) and (c, a) in zip(U, V):
                    ans += 1
    return ans

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))

    ans = 0
    for i in range(M):
        u, v = edges[i]
        for j in range(i+1, M):
            w, x = edges[j]
            if u == w or u == x or v == w or v == x:
                continue
            if (u, v) in edges and (v, w) in edges and (w, u) in edges:
                ans += 1
            if (u, v) in edges and (v, x) in edges and (x, u) in edges:
                ans += 1
            if (u, w) in edges and (w, v) in edges and (v, u) in edges:
                ans += 1
            if (u, w) in edges and (w, x) in edges and (x, u) in edges:
                ans += 1
            if (u, x) in edges and (x, v) in edges and (v, u) in edges:
                ans += 1
            if (u, x) in edges and (x, w) in edges and (w, u) in edges:
                ans += 1
            if (v, w) in edges and (w, u) in edges and (u, v) in edges:
                ans += 1
            if (v, w) in edges and (w, x) in edges and (x, v) in edges:
                ans += 1
            if (v, x) in edges and (x, u) in edges and (u, v) in edges:
                ans += 1
            if (v, x) in edges and (x, w) in edges and (w, v) in edges:
                ans += 1
            if (w, x) in edges and (x, u) in edges and (u, w) in edges:
                ans += 1
            if (w, x) in edges and (x, v) in edges and (v, w) in edges:
                ans += 1

    print(ans)

main()

=======
Suggestion 6

def is_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

=======
Suggestion 7

def main():
    N, M = map(int, raw_input().split())
    edges = []
    for i in xrange(M):
        edges.append(map(int, raw_input().split()))
    print solve(N, M, edges)

=======
Suggestion 8

def get_combination(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    return get_combination(n - 1, r) + get_combination(n - 1, r - 1)

=======
Suggestion 9

def get_input():
    N, M = map(int, input().split())
    edges = {}
    for _ in range(M):
        u, v = map(int, input().split())
        if not u in edges:
            edges[u] = set()
        if not v in edges:
            edges[v] = set()
        edges[u].add(v)
        edges[v].add(u)
    return N, M, edges

=======
Suggestion 10

def solve():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    # 1-indexed to 0-indexed
    edges = [(a - 1, b - 1) for a, b in edges]

    # create adjacency matrix
    adj = [[False for _ in range(N)] for _ in range(N)]
    for a, b in edges:
        adj[a][b] = True
        adj[b][a] = True

    # count triangles
    ans = 0
    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                if adj[a][b] and adj[b][c] and adj[c][a]:
                    ans += 1

    print(ans)
