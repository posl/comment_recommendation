def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    ans = 0
    for i in range(1, N+1):
        for j in graph[i]:
            if i < j:
                cnt = 0
                for k in graph[i]:
                    if k in graph[j]:
                        cnt += 1
                if cnt == 1:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()