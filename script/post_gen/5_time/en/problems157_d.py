Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * K
    D = [0] * K
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    friend = [0] * N
    for i in range(M):
        friend[A[i] - 1] += 1
        friend[B[i] - 1] += 1
    block = [0] * N
    for i in range(K):
        block[C[i] - 1] += 1
        block[D[i] - 1] += 1
    for i in range(N):
        print(friend[i] - block[i] - 1, end=' ')

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A, B = A-1, B-1
        friends[A].append(B)
        friends[B].append(A)
    for _ in range(K):
        C, D = map(int, input().split())
        C, D = C-1, D-1
        blocks[C].append(D)
        blocks[D].append(C)
    ans = [0]*N
    for i in range(N):
        ans[i] = len(set(friends[i]) - set(friends[i]) & set(blocks[i]))
    print(*ans)

=======
Suggestion 3

def main():
    n, m, k = map(int, input().split())
    friends = [set() for _ in range(n)]
    blocks = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a-1].add(b-1)
        friends[b-1].add(a-1)
    for _ in range(k):
        c, d = map(int, input().split())
        blocks[c-1].add(d-1)
        blocks[d-1].add(c-1)

    for i in range(n):
        print(len(friends[i] - blocks[i] - {i}) - 1, end=' ')

=======
Suggestion 4

def main():
    n, m, k = map(int, input().split())
    friends = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a-1] += 1
        friends[b-1] += 1
    blocks = [0] * n
    for _ in range(k):
        c, d = map(int, input().split())
        blocks[c-1] += 1
        blocks[d-1] += 1
    for i in range(n):
        print(friends[i] - blocks[i] - 1)

=======
Suggestion 5

def main():
    # Get input
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]

    # Make graph
    graph = [[] for _ in range(N)]
    for a, b in AB:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    # Make block graph
    block_graph = [[] for _ in range(N)]
    for c, d in CD:
        block_graph[c-1].append(d-1)
        block_graph[d-1].append(c-1)

    # Make friend candidates
    friend_candidates = [N-1 - len(graph[i]) - len(block_graph[i]) for i in range(N)]
    for i in range(N):
        for j in graph[i]:
            if i < j:
                for k in graph[j]:
                    if k in graph[i]:
                        friend_candidates[i] -= 1
                        friend_candidates[j] -= 1

    # Print
    print(*friend_candidates)

=======
Suggestion 6

def main():
    # Get input here
    N, M, K = map(int, input().strip().split())
    AB = [tuple(map(int, input().strip().split())) for _ in range(M)]
    CD = [tuple(map(int, input().strip().split())) for _ in range(K)]

    # Get output here
    print(*solve(N, M, K, AB, CD))

=======
Suggestion 7

def get_input():
    N,M,K = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    C = []
    D = []
    for i in range(K):
        c,d = map(int,input().split())
        C.append(c)
        D.append(d)
    return N,M,K,A,B,C,D

=======
Suggestion 8

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

=======
Suggestion 9

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

=======
Suggestion 10

def dfs(G, s, a, b):
    if s == b:
        return True
    for t in G[s]:
        if t == a or t == b:
            continue
        if dfs(G, t, a, b):
            return True
    return False
