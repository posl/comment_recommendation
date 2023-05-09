def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x = []
    y = []
    r = []
    for _ in range(N):
        x_, y_, r_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        r.append(r_)
    if s_x == t_x and s_y == t_y:
        print('Yes')
        return
    for i in range(N):
        if (s_x - x[i]) ** 2 + (s_y - y[i]) ** 2 < r[i] ** 2:
            for j in range(N):
                if (t_x - x[j]) ** 2 + (t_y - y[j]) ** 2 < r[j] ** 2:
                    print('Yes')
                    return
    print('No')
    return
