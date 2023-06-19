def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    graph = [[] for _ in range(n+1)]
    for a, b in ab:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n+1)
    visited[1] = True
    ans = []
    ans.append(1)
    #print(graph)
    #print(visited)
    #print(ans)
    while True:
        for i in graph[ans[-1]]:
            if visited[i] == False:
                visited[i] = True
                ans.append(i)
                break
        else:
            if ans[-1] == 1:
                break
            else:
                ans.pop(-1)
    print(*ans)

if __name__ == '__main__':
    main()