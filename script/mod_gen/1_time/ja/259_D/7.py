def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(N)]
    # 2点間の距離
    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 円と円の交差判定
    def intersect(x1, y1, r1, x2, y2, r2):
        d = dist(x1, y1, x2, y2)
        return (r1 + r2 >= d) and (abs(r1 - r2) <= d)
    # 円と点の交差判定
    def intersect_circle_point(x, y, r, px, py):
        return dist(x, y, px, py) <= r
    # 2点間の直線と円の交差判定
    def intersect_line_circle(x1, y1, x2, y2, cx, cy, r):
        d = abs((x2 - x1) * (y1 - cy) - (x1 - cx) * (y2 - y1)) / dist(x1, y1, x2, y2)
        return d <= r
    # 2点間の直線と円の交差判定
    def intersect_line_circle2(x1, y1, x2, y2, cx, cy, r):
        d = dist(x1, y1, x2, y2)
        if d == 0:
            return intersect_circle_point(x1, y1, r, cx, cy)
        else:
            t = ((cx - x1) * (x2 - x1) + (cy - y1) * (y2 - y1)) / d
            if t < 0:
                return intersect_circle_point(x1, y1, r, cx, cy)
            elif t > d:
                return intersect_circle_point(x2, y2, r, cx, cy)
            else:
                return intersect_circle_point(x1 + t *

if __name__ == '__main__':
    main()