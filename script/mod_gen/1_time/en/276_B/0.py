def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    for i in range(N):
        G[i].sort()
        print(len(G[i]), *map(lambda x: x+1, G[i]))
main()
