def solve():
    M = int(input())
    graph = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    p = list(map(int, input().split()))
    p = [i - 1 for i in p]
    def bfs(start, goal):
        visited = [False] * 9
        visited[start] = True
        queue = [start]
        while queue:
            current = queue.pop(0)
            if current == goal:
                return True
            for next in graph[current]:
                if visited[next]:
                    continue
                visited[next] = True
                queue.append(next)
        return False
    def dfs(current, goal, visited, step):
        if current == goal:
            return step
        if step == 16:
            return -1
        for next in graph[current]:
            if visited[next]:
                continue
            visited[next] = True
            tmp = dfs(next, goal, visited, step + 1)
            if tmp != -1:
                return tmp
            visited[next] = False
        return -1
    if bfs(p[0], 0):
        print(-1)
        return
    ans = -1
    for i in range(1, 8):
        visited = [False] * 9
        visited[p[i]] = True
        visited[p[0]] = True
        tmp = dfs(p[0], p[i], visited, 0)
        if tmp == -1:
            print(-1)
            return
        if ans == -1:
            ans = tmp
        else:
            ans += tmp
    print(ans)

if __name__ == '__main__':
    solve()