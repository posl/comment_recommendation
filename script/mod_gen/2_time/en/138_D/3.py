def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    #print(graph)
    #print("
")
    q = []
    for _ in range(Q):
        p, x = map(int, input().split())
        q.append((p-1, x))
    #print(q

if __name__ == '__main__':
    main()