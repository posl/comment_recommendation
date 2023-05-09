def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [tuple(map(int, input().split())) for _ in range(N)]
    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    def in_circle(x, y, circle):
        return dist(x, y, circle[0], circle[1]) <= circle[2]
    def dfs(x, y, circles):
        if in_circle(x, y, circles[0]):
            return True
        if len(circles) == 1:
            return False
        return dfs(x, y, circles[1:]) or dfs(x, y, circles[1:])
    print('Yes' if dfs(s_x, s_y, circles) and dfs(t_x, t_y, circles) else 'No')

if __name__ == '__main__':
    main()