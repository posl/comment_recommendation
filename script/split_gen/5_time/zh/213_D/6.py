def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort()
    graph = {}
    for i in range(1, N+1):
        graph[i] = []
    for a, b in AB:
        graph[a].append(b)
        graph[b].append(a)
    # bfs
    from collections import deque
    q = deque()
    q.append(1)
    visited = [False] * (N+1)
    visited[1] = True
    ans = [1]
    while q:
        c = q.popleft()
        for n in graph[c]:
            if not visited[n]:
                visited[n] = True
                ans.append(n)
                q.append(n)
                break
        else:
            ans.append(ans[-2])
    print(*ans)
