def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    G = [[] for _ in range(N+1)]
    for a,b in AB:
        G[a].append(b)
        G[b].append(a)
    from collections import deque
    q = deque([1])
    visited = [False] * (N+1)
    visited[1] = True
    ans = []
    while q:
        x = q.popleft()
        ans.append(x)
        for y in G[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)
                break
        else:
            if x == 1:
                break
            q.appendleft(x)
    print(*ans)
