def solve():
    N = int(input())
    points = []
    for i in range(N):
        x, y, p = map(int, input().split())
        points.append((x, y, p))
    def can_jump(start, end, s):
        x1, y1, p1 = points[start]
        x2, y2, p2 = points[end]
        return p1 * s >= abs(x1 - x2) + abs(y1 - y2)
    def dfs(s, visited, start):
        visited[start] = True
        for i in range(N):
            if not visited[i] and can_jump(start, i, s):
                dfs(s, visited, i)
    def can_reach_all(s):
        visited = [False] * N
        dfs(s, visited, 0)
        return all(visited)
    def binary_search():
        l = 0
        r = 10**18
        while r - l > 1:
            m = (l + r) // 2
            if can_reach_all(m):
                r = m
            else:
                l = m
        return r
    print(binary_search())
solve()

if __name__ == '__main__':
    solve()