def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    color = [-1]*N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        c = 0
        for u in G[v]:
            if color[u] != -1:
                continue
            while c == color[v] or c == color[G[v][G[v].index(u)-1]]:
                c += 1
            color[u] = c
            c += 1
            stack.append(u)
    print(max(color)+1)
    for i in range(N-1):
        print(color[i]+1)
