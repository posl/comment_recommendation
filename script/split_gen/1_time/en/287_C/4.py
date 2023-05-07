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
