def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    colors = [-1 for _ in range(n)]
    colors[0] = 0
    q = [0]
    while len(q) > 0:
        v = q.pop()
        for edge in edges:
            if edge[0] == v and colors[edge[1]-1] == -1:
                colors[edge[1]-1] = (colors[v]+edge[2])%2
                q.append(edge[1]-1)
            elif edge[1] == v and colors[edge[0]-1] == -1:
                colors[edge[0]-1] = (colors[v]+edge[2])%2
                q.append(edge[0]-1)
    for color in colors:
        print(color)
