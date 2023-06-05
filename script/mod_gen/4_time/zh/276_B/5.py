def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(n):
        print(len(graph[i]), end=" ")
        for j in sorted(graph[i]):
            print(j+1, end=" ")
        print()

if __name__ == '__main__':
    main()