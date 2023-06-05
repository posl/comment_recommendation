def bfs(start, end, n, m):
    if start == end:
        return 0
    queue = [start]
    visited = [[0 for i in range(n)] for j in range(n)]
    visited[start[0]][start[1]] = 1
    step = 0
    while len(queue) != 0:
        step += 1
        for i in range(len(queue)):
            cur = queue.pop(0)
            for j in range(4):
                next = (cur[0] + direction[j][0], cur[1] + direction[j][1])
                if 0 <= next[0] < n and 0 <= next[1] < n and visited[next[0]][next[1]] == 0:
                    visited[next[0]][next[1]] = 1
                    if next == end:
                        return step
                    queue.append(next)
    return -1
n, m = map(int, input().split())
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for i in range(n):
    for j in range(n):
        start = (0, 0)
        end = (i, j)
        print(bfs(start, end, n, m), end=' ')
    print()

if __name__ == '__main__':
    bfs()