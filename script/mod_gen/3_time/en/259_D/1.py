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
    if N == 1:
        if (s_x - x[0])**2 + (s_y - y[0])**2 < r[0]**2 and (t_x - x[0])**2 + (t_y - y[0])**2 < r[0]**2:
            print('Yes')
        else:
            print('No')
    else:
        if (s_x - x[0])**2 + (s_y - y[0])**2 < r[0]**2:
            for i in range(1, N):
                if (t_x - x[i])**2 + (t_y - y[i])**2 < r[i]**2:
                    print('Yes')
                    exit()
        elif (s_x - x[1])**2 + (s_y - y[1])**2 < r[1]**2:
            for i in range(1, N):
                if (t_x - x[i])**2 + (t_y - y[i])**2 < r[i]**2:
                    print('Yes')
                    exit()
        else:
            print('No')

if __name__ == '__main__':
    main()