def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(N)]
    def check(x, y):
        for circle in circles:
            if (x - circle[0])**2 + (y - circle[1])**2 >= circle[2]**2:
                return False
        return True
    def bfs():
        from collections import deque
        q = deque()
        q.append((s_x, s_y))
        visited = set()
        while q:
            x, y = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if check(nx, ny) and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
        return (t_x, t_y) in visited
    print("Yes" if bfs() else "No")

if __name__ == '__main__':
    main()