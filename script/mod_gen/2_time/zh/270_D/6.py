def main():
    N, X, Y = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(N-1):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    #print(graph)
    #print(X, Y)
    #print(graph[X-1])
    #print(graph[Y-1])
    for i in range(N):
        if X-1 in graph[i]:
            #print(i)
            if Y-1 in graph[i]:
                print(i+1, end=' ')
                print(X, end=' ')
                print(Y, end=' ')
                break
            else:
                print(i+1, end=' ')
                print(X, end=' ')
                break
    for i in range(N):
        if Y-1 in graph[i]:
            if X-1 in graph[i]:
                break
            else:
                print(Y, end=' ')
                break
    print()

if __name__ == '__main__':
    main()