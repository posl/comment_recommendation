def main():
    import sys
    from collections import deque
    def input():
        return sys.stdin.readline()[:-1]
    M = int(input())
    graph = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    pieces = list(map(int, input().split()))
    for i in range(8):
        pieces[i] -= 1
    empty = 8
    for i in range(9):
        if i not in pieces:
            empty = i
            break
    def bfs(start, goal):
        queue = deque()
        queue.append(start)
        visited = [False] * 9
        visited[start] = True
        while queue:
            now = queue.popleft()
            if now == goal:
                return True
            for next in graph[now]:
                if visited[next]:
                    continue
                visited[next] = True
                queue.append(next)
        return False
    def dfs(now, visited, count):
        if count == 8:
            return True
        for next in range(9):
            if next in visited:
                continue
            if next == empty:
                continue
            if next not in graph[now]:
                continue
            visited.add(next)
            if dfs(next, visited, count + 1):
                return True
            visited.remove(next)
        return False
    for i in range(8):
        if not bfs(pieces[i], i):
            print(-1)
            return
        if not bfs(empty, pieces[i]):
            print(-1)
            return
    for i in range(8):
        if not bfs(pieces[i], empty):
            print(-1)
            return
    for i in range(8):
        if not bfs(pieces[i], pieces[(i + 1) % 8]):
            print(-1)
            return
    if dfs(empty, set(), 0):
        print(0)
        return
    print(8)

if __name__ == '__main__':
    main()