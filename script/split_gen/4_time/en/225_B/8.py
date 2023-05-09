def main():
    N = int(input())
    N_edges = N - 1
    edges = []
    for i in range(N_edges):
        a, b = map(int, input().split())
        edges.append([a, b])
    #print(N)
    #print(edges)
    degree = [0 for i in range(N)]
    for i in range(N_edges):
        degree[edges[i][0] - 1] += 1
        degree[edges[i][1] - 1] += 1
    #print(degree)
    if degree.count(1) == 1 and degree.count(N - 1) == 1:
        print('Yes')
    else:
        print('No')
