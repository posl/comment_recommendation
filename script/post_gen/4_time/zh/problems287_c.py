Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n, m = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, n + 1):
        if len(graph[i]) > 2:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    edge = []
    for i in range(M):
        edge.append(list(map(int, input().split())))
    edge.sort()
    v = [0] * N
    for i in range(M):
        v[edge[i][0]-1] += 1
        v[edge[i][1]-1] += 1
    if max(v) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    for i in range(N):
        if len(graph[i]) > 2:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 5

def is_path_graph(n,m,edges):
    if m != n-1:
        return False
    for i in range(1,n+1):
        if len(edges[i]) != 2:
            return False
    return True

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges = sorted(edges, key=lambda x: x[0])
    # print(edges)
    flag = True
    for i in range(len(edges)-1):
        if edges[i][1] != edges[i+1][0]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    if M != N-1:
        print("No")
        return

    edges = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    for i in range(1, N+1):
        if len(edges[i]) > 2:
            print("No")
            return

    print("Yes")

main()

=======
Suggestion 8

def get_input():
    N, M = input().split()
    N = int(N)
    M = int(M)
    print(N, M)
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = input().split()
        u[i] = int(u[i])
        v[i] = int(v[i])
        print(u[i], v[i])
    return N, M, u, v
