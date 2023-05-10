def main():
    # Get input
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    # Make graph
    graph = [[] for _ in range(N)]
    for a, b in AB:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    # Make block graph
    block_graph = [[] for _ in range(N)]
    for c, d in CD:
        block_graph[c-1].append(d-1)
        block_graph[d-1].append(c-1)
    # Make friend candidates
    friend_candidates = [N-1 - len(graph[i]) - len(block_graph[i]) for i in range(N)]
    for i in range(N):
        for j in graph[i]:
            if i < j:
                for k in graph[j]:
                    if k in graph[i]:
                        friend_candidates[i] -= 1
                        friend_candidates[j] -= 1
    # Print
    print(*friend_candidates)
