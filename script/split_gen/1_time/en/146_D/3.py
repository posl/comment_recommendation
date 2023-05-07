def main():
    N = int(input())
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    print(N-1)
    for i in range(1,N+1):
        for j in G[i]:
            if i < j:
                print(G[i].index(j))
