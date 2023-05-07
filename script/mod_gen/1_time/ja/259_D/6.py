def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [tuple(map(int, input().split())) for _ in range(N)]
    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    def is_ok(x, y):
        for x0, y0, r in circles:
            if dist(x, y, x0, y0) <= r:
                return True
        return False
    def is_ok2(x, y):
        for x0, y0, r in circles:
            if dist(x, y, x0, y0) <= r:
                return False
        return True
    if is_ok(s_x, s_y) and is_ok(t_x, t_y):
        print("Yes")
        return
    if is_ok2(s_x, s_y) and is_ok2(t_x, t_y):
        print("No")
        return
    def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
        # 線分 (x1, y1) -> (x2, y2) と線分 (x3, y3) -> (x4, y4) が交差しているかどうか
        def ccw(x1, y1, x2, y2, x3, y3):
            # (x1, y1) -> (x2, y2) -> (x3, y3) の順に進むときの方向
            # 1: 反時計回り
            # 0: 線上
            # -1: 時計回り
            return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        return ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3

if __name__ == '__main__':
    main()