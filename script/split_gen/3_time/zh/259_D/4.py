def main():
    N = int(input())
    S_X, S_Y, T_X, T_Y = map(int, input().split())
    circles = []
    for _ in range(N):
        circles.append(list(map(int, input().split())))
    def check(x, y):
        for i in range(N):
            if (x - circles[i][0]) ** 2 + (y - circles[i][1]) ** 2 > circles[i][2] ** 2:
                return False
        return True
    def solve():
        for i in range(N):
            if check(circles[i][0], circles[i][1]):
                return True
        return False
    if solve():
        print('Yes')
    else:
        print('No')
