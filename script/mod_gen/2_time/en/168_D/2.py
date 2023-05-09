def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    # BFS
    from collections import deque
    que = deque()
    que.append(1)
    dist = [-1] * (N + 1)
    dist[1] = 0
    while que:
        p = que.popleft()
        for q in graph[p]:
            if dist[q] != -1:
                continue
            dist[q] = dist[p] + 1
            que.append(q)
    # 1 からの距離が偶数の時は 1 に向かう
    # 奇数の時は 1 に向かわない
    ans = []
    for i in range(2, N + 1):
        if dist[i] % 2 == 0:
            ans.append(1)
        else:
            ans.append(i)
    print("Yes")
    print(*ans, sep="
")

if __name__ == '__main__':
    main()