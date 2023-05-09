def main():
    M = int(input())
    graph = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    pos = list(map(int, input().split()))
    pos = [p-1 for p in pos]
    empty = 8
    for p in pos:
        if p == 8:
            empty = 8
            break
    for i in range(9):
        if i in pos:
            continue
        empty = i
        break
    graph[empty].append(empty)
    graph[empty].sort()
    def dfs(v, visited):
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                dfs(u, visited)
    visited = set()
    dfs(empty, visited)
    if len(visited) != 9:
        print(-1)
        return
    def dfs2(v, visited):
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                dfs2(u, visited)
    visited = set()
    dfs2(pos[0], visited)
    if len(visited) != 9:
        print(-1)
        return
    def dfs3(v, visited):
        visited.add(v)
        for u in graph[v]:
            if u not in visited:
                dfs3(u, visited)
    visited = set()
    dfs3(pos[1], visited)
    if len(visited) != 9:
        print(-1)
        return
    def bfs(v, visited):
        q = [v]
        while q:
            v = q.pop()
            visited.add(v)
            for u in graph[v]:
                if u not in visited:
                    q.append(u)
    visited = set()
    bfs(empty, visited)
    if len(visited) != 9:
        print(-1)
        return
    def bfs2(v, visited):
        q = [v]
        while q:
            v = q.pop()
            visited.add(v)
            for u in graph[v]:
                if u not in visited:
                    q.append(u)
    visited = set()
    bfs2(pos[0], visited)
    if len(visited) != 9:
        print(-1)
        return

if __name__ == '__main__':
    main()