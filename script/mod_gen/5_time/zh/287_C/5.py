def main():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    for i in range(n):
        graph[i].sort()
    for i in range(n):
        if graph[i] != list(range(min(i+2,n),max(i-1,0),-1)):
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()