def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    if len(graph[1]) == 1 and len(graph[N]) == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()