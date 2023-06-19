def main():
    # 读取输入
    n = int(input("请输入一个由数字1和9组成的整数(111 ≦ n ≦ 999)："))
    # 计算
    n = 1110 - n
    # 输出结果
    print(n)

if __name__ == '__main__':
    main()