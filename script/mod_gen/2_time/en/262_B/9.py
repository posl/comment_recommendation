def main():
    N, M = map(int, input().split(' '))
    edges = [list(map(int, input().split(' '))) for _ in range(M)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    ans = 0
    for a in range(N):
        for b in graph[a]:
            if a >= b:
                continue
            for c in graph[b]:
                if a >= c:
                    continue
                if b in graph[c]:
                    ans += 1
    print(ans // 3)

if __name__ == '__main__':
    main()