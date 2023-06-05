def main():
    # 读入数据
    k = int(input())
    # 初始值
    s = 0
    # 循环
    for i in range(1, k+1):
        s = s * 10 + 7
        s %= k
        # 如果余数为0
        if s == 0:
            print(i)
            exit()
    # 如果没有余数为0的情况
    print(-1)

if __name__ == '__main__':
    main()