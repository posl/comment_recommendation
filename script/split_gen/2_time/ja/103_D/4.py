def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))
    edges.sort()
    #print(edges)
    #edges = [(1, 4), (2, 5)]
    #print(edges[0][0])
    #print(edges[0][1])
    #print(edges[1][0])
    #print(edges[1][1])
    #print(edges[1][0] - edges[0][1])
    #print(edges[1][0] - edges[0][1] - 1)
    #print(edges[0][1] - edges[0][0])
    #print(edges[1][1] - edges[1][0])
    ans = 0
    for i in range(M):
        if i == 0:
            ans += edges[0][1] - edges[0][0]
        else:
            ans += edges[i][1] - edges[i][0] - (edges[i][0] - edges[i-1][1] - 1)
    print(ans)
