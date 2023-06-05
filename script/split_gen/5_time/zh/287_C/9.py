def main():
    n,m = map(int, input().split())
    if m != n-1:
        print("No")
        return
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    for i in range(n):
        graph[i].sort()
    for i in range(n):
        if graph[i] != [i-1,i+1]:
            print("No")
            return
    print("Yes")
