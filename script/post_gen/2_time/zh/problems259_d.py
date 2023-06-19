Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for i in range(N):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    print('Yes')

=======
Suggestion 3

def solve():
    return

=======
Suggestion 4

def main():
    n = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    xyr = [list(map(int, input().split())) for _ in range(n)]
    # print(xyr)
    # print(s_x, s_y, t_x, t_y)
    # print(xyr[0][0], xyr[0][1], xyr[0][2])
    s = [s_x, s_y]
    t = [t_x, t_y]
    # print(s)
    # print(t)
    # print(xyr[0][0], xyr[0][1], xyr[0][2])
    # print(xyr[1][0], xyr[1][1], xyr[1][2])
    # print(xyr[2][0], xyr[2][1], xyr[2][2])
    # print(xyr[3][0], xyr[3][1], xyr[3][2])
    # print(xyr[4][0], xyr[4][1], xyr[4][2])
    # print(xyr[5][0], xyr[5][1], xyr[5][2])
    # print(xyr[6][0], xyr[6][1], xyr[6][2])
    # print(xyr[7][0], xyr[7][1], xyr[7][2])
    # print(xyr[8][0], xyr[8][1], xyr[8][2])
    # print(xyr[9][0], xyr[9][1], xyr[9][2])
    # print(xyr[10][0], xyr[10][1], xyr[10][2])
    # print(xyr[11][0], xyr[11][1], xyr[11][2])
    # print(xyr[12][0], xyr[12][1], xyr[12][2])
    # print(xyr[13][0], xyr[13][1], xyr[13][2])
    # print(xyr[14][0], xyr[14][1], xyr[14][2])
    # print(xyr[15][0], xyr[15][1], x

=======
Suggestion 5

def check(x, y, circles):
    for circle in circles:
        if (x-circle[0])**2+(y-circle[1])**2 < circle[2]**2:
            return True
    return False

=======
Suggestion 6

def solve():
    pass

=======
Suggestion 7

def main():
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for i in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    print("Yes" if solve(n, sx, sy, tx, ty, circles) else "No")
