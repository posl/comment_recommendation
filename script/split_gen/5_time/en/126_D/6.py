def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        edges.append(list(map(int, input().split())))
    nodes = [-1 for i in range(N+1)]
    nodes[1] = 0
    for edge in edges:
        if nodes[edge[0]] == -1:
            nodes[edge[0]] = nodes[edge[1]] + edge[2]
        elif nodes[edge[1]] == -1:
            nodes[edge[1]] = nodes[edge[0]] + edge[2]
        else:
            nodes[edge[0]] = nodes[edge[1]] + edge[2]
    for i in range(1, N+1):
        print(nodes[i]%2)
