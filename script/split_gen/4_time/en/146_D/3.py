def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    adj = [[] for _ in range(N)]
    for a, b in edges:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    colors = [-1] * N
    colors[0] = 0
    for i in range(N):
        color = 0
        for j in adj[i]:
            if colors[j] == color:
                color += 1
        for j in adj[i]:
            if colors[j] == -1:
                colors[j] = color
                color += 1
    print(max(colors)+1)
    for i in range(N-1):
        print(colors[edges[i][0]-1]+1)
