def get_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        edge = list(map(int,input().split()))
        edges.append(edge)
    return n, edges
