def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x = []
    y = []
    r = []
    for i in range(N):
        x_i, y_i, r_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        r.append(r_i)
    #print(x)
    #print(y)
    #print(r)
    #print(s_x, s_y, t_x, t_y)
    #print(N)
    # 2点間の距離
    def distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 2点間の距離がr1+r2より短ければ接する
    for i in range(N):
        if distance(s_x, s_y, x[i], y[i]) + distance(t_x, t_y, x[i], y[i]) < distance(s_x, s_y, t_x, t_y) + r[i]:
            print("Yes")
            exit()
    print("No")
