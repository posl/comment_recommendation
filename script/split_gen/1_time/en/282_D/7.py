def main():
    # Read input
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    # Create adjacency list
    adj = [[] for _ in range(N)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    # Create a bipartite graph
    bip = [1] * N
    for i in range(N):
        if bip[i] == 1:
            bip[i] = 0
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if bip[v] == 1:
                        bip[v] = 0 if bip[u] == 1 else 1
                        stack.append(v)
                    elif bip[v] == bip[u]:
                        print(0)
                        return
    # Count the number of pairs of integers (u, v) that satisfy the conditions in the problem statement
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if bip[i] != bip[j] and j not in adj[i]:
                ans += 1
    print(ans)
