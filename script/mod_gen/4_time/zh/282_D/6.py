def main():
    n,m = map(int,input().split())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    ans = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if j in graph[i]:
                continue
            for k in graph[i]:
                if k in graph[j]:
                    break
            else:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()