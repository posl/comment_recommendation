def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    M = int(input())
    graph = [[] for _ in range(10)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, 10):
        graph[i].append(i)
    pos = list(map(int, input().split()))
    for i in range(8):
        pos[i] = [pos[i], i + 1]
    # 連結判定
    def dfs(v):
        seen[v] = True
        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)
    seen = [False] * 10
    dfs(1)
    if not all(seen):
        print(-1)
        return
    # 8パズルの距離を求める
    def bfs():
        q = deque()
        q.append(pos)
        d = {(tuple(pos)): 0}
        while q:
            v = q.popleft()
            if v == [[1], [2], [3], [4], [5], [6], [7], [8]]:
                return d[tuple(v)]
            for i in range(8):
                for j in range(8):
                    if i == j:
                        continue
                    if v[i][0] in graph[v[j][0]]:
                        new_v = v[:]
                        new_v[i], new_v[j] = new_v[j], new_v[i]
                        new_v[i].insert(0, new_v[i].pop())
                        new_v[j].insert(0, new_v[j].pop())
                        if tuple(new_v) not in d:
                            d[tuple(new_v)] = d[tuple(v)] + 1
                            q.append(new_v)
        return -1
    print(bfs())

if __name__ == '__main__':
    main()