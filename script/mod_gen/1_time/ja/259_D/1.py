def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x = []
    y = []
    r = []
    for i in range(N):
        x_, y_, r_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
        r.append(r_)
    print(solve(N, s_x, s_y, t_x, t_y, x, y, r))

if __name__ == '__main__':
    main()