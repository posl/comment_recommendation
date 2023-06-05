def problem200_b():
    # 读取输入
    str = input()
    str = str.split(" ")
    N = int(str[0])
    K = int(str[1])
    # 循环K次
    for i in range(K):
        # 如果N是200的倍数，就用它除以200。
        if N % 200 == 0:
            N = N // 200
        else:
            # 否则，将N看作一个字符串，并在它的末尾加上200。
            N = int(str(N) + "200")
    # 打印出所得的整数
    print(N)

if __name__ == '__main__':
    problem200_b()