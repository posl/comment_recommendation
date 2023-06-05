def is_convex(a, b, c, d):
    # 用叉积判断
    def cross(x1, y1, x2, y2):
        return x1*y2 - x2*y1
    def cross_product(x1, y1, x2, y2, x3, y3):
        return cross(x2-x1, y2-y1, x3-x1, y3-y1)
    def same_side(x1, y1, x2, y2, x3, y3, x4, y4):
        return cross_product(x1, y1, x2, y2, x3, y3) * cross_product(x1, y1, x2, y2, x4, y4) >= 0
    return same_side(a[0], a[1], b[0], b[1], c[0], c[1], d[0], d[1]) and \
           same_side(b[0], b[1], c[0], c[1], d[0], d[1], a[0], a[1]) and \
           same_side(c[0], c[1], d[0], d[1], a[0], a[1], b[0], b[1]) and \
           same_side(d[0], d[1], a[0], a[1], b[0], b[1], c[0], c[1])
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]
