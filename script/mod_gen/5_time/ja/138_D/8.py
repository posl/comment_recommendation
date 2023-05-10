def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p-1] += x
    stack = [0]
    visited = [False] * N
    visited[0] = True
    while stack:
        v = stack.pop()
        for e in edge[v]:
            if visited[e]:
                continue
            counter[e] += counter[v]
            visited[e] = True
            stack.append(e)
    print(*counter)

if __name__ == '__main__':
    main()