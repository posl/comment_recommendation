def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [tuple(map(int, input().split())) for _ in range(N)]
    # print(N, s_x, s_y, t_x, t_y, circles)
    def dist2(x1, y1, x2, y2):
        return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    def in_circle(x, y, circle):
        x0, y0, r = circle
        return dist2(x, y, x0, y0) <= r * r
    def dfs(x, y, visited):
        if in_circle(x, y, circles[0]): return True
        if in_circle(x, y, circles[1]): return True
        if in_circle(x, y, circles[2]): return True
        if in_circle(x, y, circles[3]): return True
        visited.add((x, y))
        for cx, cy, cr in circles:
            dx = cx - x
            dy = cy - y
            if dx == 0 and dy == 0: continue
            if dx == 0:
                if dy > 0:
                    nx = x
                    ny = y + cr
                else:
                    nx = x
                    ny = y - cr
            elif dy == 0:
                if dx > 0:
                    nx = x + cr
                    ny = y
                else:
                    nx = x - cr
                    ny = y
            else:
                if dx > 0:
                    nx = x + cr
                else:
                    nx = x - cr
                if dy > 0:
                    ny = y + cr
                else:
                    ny = y - cr
            if (nx, ny) in visited: continue
            if dfs(nx, ny, visited): return True
        return False
    if dfs(s_x, s_y, set()):
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()