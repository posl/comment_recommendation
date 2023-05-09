def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    if M != N-1:
        print("No")
        return
    for i in range(N):
        if len(G[i]) != 2:
            print("No")
            return
    print("Yes")
