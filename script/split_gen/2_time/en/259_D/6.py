def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    def is_on_circumference(x, y, circle):
        cx, cy, r = circle
        return (x - cx) ** 2 + (y - cy) ** 2 == r ** 2
    def is_between(x, y, circle1, circle2):
        return is_on_circumference(x, y, circle1) and is_on_circumference(x, y, circle2)
    # (sx, sy) と (tx, ty) の間には少なくとも１つの円がある
    # つまり、(sx, sy) と (tx, ty) の間には少なくとも２つの円がある
    # その２つの円のうち、１つは (sx, sy) の円である
    # よって、(sx, sy) と (tx, ty) の間にある円は、(sx, sy) の円と (tx, ty) の円の２つだけである
    # つまり、(sx, sy) と (tx, ty) の間にある円のうち、(sx, sy) の円を除いた１つの円が、(tx, ty) の円である
    # この円の中心から (sx, sy) と (tx, ty) が等距離になっている
    # つまり、(sx, sy) と (tx, ty) の間にある円のうち、(sx, sy) の円を除いた１つの円が、(tx, ty) の円である
    # この円の中心から (sx, sy) と (tx, ty) が等距離になっている
    # つまり、(sx, sy) と (tx, ty) の間にある円
