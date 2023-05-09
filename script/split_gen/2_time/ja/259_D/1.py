def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    x, y, r = [], [], []
    for _ in range(N):
        xi, yi, ri = map(int, input().split())
        x.append(xi)
        y.append(yi)
        r.append(ri)
    # 2円の交点を求める
    def get_cross_points(x1, y1, r1, x2, y2, r2):
        if r1 < r2:
            x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if d == 0:
            return []
        if d > r1 + r2 or d < abs(r1 - r2):
            return []
        a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
        h = (r1 ** 2 - a ** 2) ** 0.5
        x3 = x1 + a * (x2 - x1) / d
        y3 = y1 + a * (y2 - y1) / d
        x4 = x3 + h * (y2 - y1) / d
        y4 = y3 - h * (x2 - x1) / d
        x5 = x3 - h * (y2 - y1) / d
        y5 = y3 + h * (x2 - x1) / d
        return [(x4, y4), (x5, y5)]
    # 2点間の距離を求める
    def get_distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 2点間の距離が円の半径よりも短いかどうかを判定する
    def is_shorter(x1, y1
