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
