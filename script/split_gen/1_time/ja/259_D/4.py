def main():
    #入力
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x = [0 for i in range(N)]
    y = [0 for i in range(N)]
    r = [0 for i in range(N)]
    for i in range(N):
        x[i], y[i], r[i] = map(int, input().split())
    #出力
    if (s_x - t_x) ** 2 + (s_y - t_y) ** 2 <= (r[0] + r[1]) ** 2:
        print("Yes")
    else:
        print("No")
