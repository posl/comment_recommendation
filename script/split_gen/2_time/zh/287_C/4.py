def main():
    N, M = map(int, input().split())
    G = [[] for i in range(N+1)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    for i in range(1, N+1):
        if len(G[i]) > 2:
            print("No")
            return
    print("Yes")
