def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for i in range(n):
        if len(graph[i]) > 2:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()