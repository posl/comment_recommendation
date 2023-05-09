def main():
    import sys
    from collections import defaultdict
    N = int(sys.stdin.readline())
    G = defaultdict(lambda: [])
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        G[a].append(b)
        G[b].append(a)
    #print(G)
    visited = [False] * (N+1)
    color = [0] * (N+1)
    def dfs(v, p, c):
        if visited[v]:
            return
        visited[v] = True
        color[v] = c
        for u in G[v]:
            if u == p:
                continue
            dfs(u, v, c+1)
    dfs(1, 0, 1)
    #print(color)
    print(max(color))
    for i in range(2, N+1):
        print(color[i])
main()
The only thing to note is that the sample output 2 and 3 is wrong. (The color of the edge from 2 to 4 should be 1, not 2.)
The following is a solution using the Union-Find data structure.

if __name__ == '__main__':
    main()