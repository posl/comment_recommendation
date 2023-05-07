def main():
    N = int(input())
    edges = [list(map(int,input().split())) for _ in range(N-1)]
    edge_color = [0]*(N-1)
    color = [0]*(N+1)
    for i in range(N-1):
        a,b = edges[i]
        if color[a] == color[b]:
            edge_color[i] = 1
        else:
            edge_color[i] = min(color[a],color[b])
        color[a] = color[b] = edge_color[i] + 1
    print(max(edge_color))
    for c in edge_color:
        print(c)
