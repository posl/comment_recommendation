def main():
    n,x,y = map(int,input().split())
    x -= 1
    y -= 1
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    #print(graph)
