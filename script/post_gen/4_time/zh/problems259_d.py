Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_in_circle(x, y, circles):
    for circle in circles:
        if (x-circle[0])**2 + (y-circle[1])**2 <= circle[2]**2:
            return True
    return False

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for i in range(n):
        x, y, r = map(int, input().split())
        circles.append([x, y, r])
    print(solve(circles, sx, sy, tx, ty))

=======
Suggestion 4

def isPassable(s_x, s_y, t_x, t_y, x, y, r):
    if s_x == t_x and s_y == t_y:
        return True

    # 两点连线方程
    a = s_y - t_y
    b = t_x - s_x
    c = s_x * t_y - t_x * s_y

    # 圆心到直线距离
    d = abs(a * x + b * y + c) / (a ** 2 + b ** 2) ** 0.5
    if d > r:
        return False

    # 两点距离
    dis = ((s_x - t_x) ** 2 + (s_y - t_y) ** 2) ** 0.5
    if dis <= r:
        return True

    return False

=======
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def main():
    print("Hello World!")
