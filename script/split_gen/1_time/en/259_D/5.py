def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [tuple(map(int, input().split())) for _ in range(N)]
    if (s_x, s_y) == (t_x, t_y):
        print("Yes")
        return
    for i in range(N):
        if abs((s_x - circles[i][0]) ** 2 + (s_y - circles[i][1]) ** 2 - circles[i][2] ** 2) <= 1e-6:
            for j in range(N):
                if abs((t_x - circles[j][0]) ** 2 + (t_y - circles[j][1]) ** 2 - circles[j][2] ** 2) <= 1e-6:
                    print("Yes")
                    return
    print("No")
