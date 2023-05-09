def main():
    n = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    c = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        c.append((x, y, r))
    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    def is_in_circle(x1, y1, x2, y2, r):
        return dist(x1, y1, x2, y2) < r
    def is_in_circle2(x, y, c):
        return dist(x, y, c[0], c[1]) < c[2]
    def is_in_circle3(x, y, c):
        return dist(x, y, c[0], c[1]) + c[2] < 10 ** 9
    def is_in_circle4(x, y, c):
        return dist(x, y, c[0], c[1]) < 10 ** 9 - c[2]
    def is_cross_circle(x1, y1, x2, y2, x3, y3, r):
        if dist(x1, y1, x3, y3) < r and dist(x2, y2, x3, y3) < r:
            return False
        if dist(x1, y1, x3, y3) > r and dist(x2, y2, x3, y3) > r:
            return False
        return True
    def is_cross_circle2(x1, y1, x2, y2, c):
        return is_cross_circle(x1, y1, x2, y2, c[0], c[1], c[2])
    def is_cross_circle3(x1, y1, x2, y2, c):
        return is_cross_circle(x1, y1, x2, y2, c[0], c[1], 10 ** 9 - c[2])
    if is_in_circle(s_x, s_y, t_x, t_y, 10 ** 9):
        print("Yes")
        return
    for i in range(n
