def main():
    N = int(input())
    # x = []
    # y = []
    # p = []
    # for i in range(N):
    #     x_i, y_i, p_i = map(int, input().split())
    #     x.append(x_i)
    #     y.append(y_i)
    #     p.append(p_i)
    # print(x)
    # print(y)
    # print(p)
    # for i in range(N):
    #     for j in range(N):
    #         if i == j:
    #             continue
    #         else:
    #             if p[i] * S >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
    #                 continue
    #             else:
    #                 S += 1
    # print(S)
    # print(x)
    # print(y)
    # print(p)
    # print(S)
    x = []
    y = []
    p = []
    for i in range(N):
        x_i, y_i, p_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        p.append(p_i)
    S = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                if p[i] * S >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                    continue
                else:
                    S += 1
    print(S)

if __name__ == '__main__':
    main()