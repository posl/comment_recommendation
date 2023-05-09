def main():
    points = []
    for i in range(4):
        points.append(list(map(int, input().split())))
    # 外積を求める
    def cross(a, b):
        return a[0] * b[1] - a[1] * b[0]
    # 2つのベクトルの外積を求める
    def cross2(p1, p2, p3):
        return cross([p2[0] - p1[0], p2[1] - p1[1]], [p3[0] - p1[0], p3[1] - p1[1]])
    # 2つのベクトルが反時計回りかどうか判定する
    def ccw(p1, p2, p3):
        return cross2(p1, p2, p3) > 0
    # 2つのベクトルが時計回りかどうか判定する
    def cw(p1, p2, p3):
        return cross2(p1, p2, p3) < 0
    # 2つのベクトルが直線上にあるかどうか判定する
    def collinear(p1, p2, p3):
        return cross2(p1, p2, p3) == 0
    # 2つのベクトルが同じ向きかどうか判定する
    def same_direction(p1, p2, p3, p4):
        return cross([p2[0] - p1[0], p2[1] - p1[1]], [p4[0] - p3[0], p4[1] - p3[1]]) == 0
    # 2つの線分が交差するかどうか判定する
    def intersect(p1, p2, p3, p4):
        if collinear(p1, p2, p3) or collinear(p1, p2, p4) or collinear(p3, p4, p1) or collinear(p3, p4, p2):
            return
