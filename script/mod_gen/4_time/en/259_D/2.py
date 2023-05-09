def solve():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = []
    for i in range(N):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    def is_connected(c1, c2):
        x1, y1, r1 = c1
        x2, y2, r2 = c2
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2:
            return True
        else:
            return False
    def is_reachable(c1, c2):
        x1, y1, r1 = c1
        x2, y2, r2 = c2
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 - r2) ** 2:
            return True
        else:
            return False
    def is_in_circle(c, x, y):
        x1, y1, r1 = c
        if (x1 - x) ** 2 + (y1 - y) ** 2 <= r1 ** 2:
            return True
        else:
            return False
    def is_reachable_from_start(c):
        x, y, r = c
        if is_in_circle(c, s_x, s_y):
            return True
        else:
            return False
    def is_reachable_to_goal(c):
        x, y, r = c
        if is_in_circle(c, t_x, t_y):
            return True
        else:
            return False
    def is_reachable_from_start_to_goal(c1, c2):
        return is_reachable_from_start(c1) and is_reachable_to_goal(c2)
    def is_reachable_from_goal_to_start(c1, c2):
        return is_reachable_from_start(c2) and is_reachable_to_goal(c1)
    def is_reachable_from_start_to_start(c1, c2):
        return is_reachable_from_start(c1) and is_reachable_from_start(c2)
    def is_reachable_to_goal_to_goal(c1, c2):
        return is_reachable_to_goal(c1

if __name__ == '__main__':
    solve()