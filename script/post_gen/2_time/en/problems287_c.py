Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    print("Yes" if len(set(sum(edges, ()))) == N else "No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    if N - 1 == M:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print("No")
        return
    S = set()
    for i in range(M):
        u, v = map(int, input().split())
        S.add((u, v))
        S.add((v, u))
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if (i, j) not in S:
                print("No")
                return
    print("Yes")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M == N - 1:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    d = [0] * N
    for _ in range(M):
        u, v = map(int, input().split())
        d[u - 1] += 1
        d[v - 1] += 1
    for i in range(N):
        if d[i] != 2:
            print('No')
            return
    print('Yes')

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    visited = [False] * N
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        if visited[u] or visited[v]:
            print('No')
            return
        visited[u] = True
        visited[v] = True
    print('Yes')

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print('No')
        return
    v = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        v[u - 1] += 1
        v[v - 1] += 1
    for i in v:
        if i != 1:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    if n == m:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    if m != n - 1:
        print("No")
        return
    edge = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        edge[u].append(v)
        edge[v].append(u)
    for i in range(1, n + 1):
        if len(edge[i]) != 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    import sys
    N, M = map(int, input().split())
    if M == N - 1:
        for _ in range(M):
            u, v = map(int, input().split())
            if abs(u - v) > 1:
                print("No")
                sys.exit()
        print("Yes")
    else:
        print("No")
