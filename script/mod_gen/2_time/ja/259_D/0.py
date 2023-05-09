def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    R = [0] * N
    for i in range(N):
        x, y, r = map(int, input().split())
        X[i] = x
        Y[i] = y
        R[i] = r
    s = [s_x, s_y]
    t = [t_x, t_y]
    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    def is_in_circle(x, y, x_c, y_c, r):
        return dist(x, y, x_c, y_c) < r
    def is_in_circles(x, y):
        for i in range(N):
            if is_in_circle(x, y, X[i], Y[i], R[i]):
                return True
        return False
    def is_on_circles(x, y):
        for i in range(N):
            if abs(dist(x, y, X[i], Y[i]) - R[i]) < 0.0000001:
                return True
        return False
    def is_on_circle(x, y, x_c, y_c, r):
        return abs(dist(x, y, x_c, y_c) - r) < 0.0000001
    def is_on_circles(x, y):
        for i in range(N):
            if is_on_circle(x, y, X[i], Y[i], R[i]):
                return True
        return False
    def is_on_line(x, y, x1, y1, x2, y2):
        if is_on_circles(x, y):
            return False
        if is_in_circles(x, y):
            return False
        if x1 == x2:
            return abs(x - x1) < 0.0000001
        if y1 == y2:
            return abs(y - y1) < 0.0000001
        return abs((x - x1) / (x2 - x1) - (y - y1) / (y2 -

if __name__ == '__main__':
    main()