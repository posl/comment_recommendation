def read_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        u,v,w = map(int,input().split())
        edges.append((w,u,v))
    return n,edges
