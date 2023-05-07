def main():
    N,X,Y = map(int,input().split())
    X -= 1
    Y -= 1
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    ans = [-1]*N
    ans[X] = 0
    queue = [X]
    while queue:
        v = queue.pop(0)
        for nv in graph[v]:
            if ans[nv] != -1:continue
            ans[nv] = ans[v] + 1
            queue.append(nv)
    print(*ans[Y:Y+1])

if __name__ == '__main__':
    main()