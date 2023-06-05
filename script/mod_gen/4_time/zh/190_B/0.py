def main():
    # 读取输入
    n, s, d = map(int, input().split())
    # print(n, s, d)
    # print(type(n), type(s), type(d))
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    # print(x)
    # print(y)
    # print(type(x), type(y))
    # 处理
    flag = 0
    for i in range(n):
        if x[i] < s and y[i] > d:
            flag = 1
            break
    # 输出
    if flag == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()