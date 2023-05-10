def solve():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    graph = [[] for _ in range(N+1)]
    for a, b in AB:
        graph[a].append(b)
        graph[b].append(a)
    dist = [-1] * (N+1)
    dist[1] = 0
    stack = [1]
    while stack:
        now = stack.pop()
        for next in graph[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                stack.append(next)
    for c, d in CD:
        if abs(dist[c] - dist[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    solve()