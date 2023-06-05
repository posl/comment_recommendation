def main():
    # 读取输入
    a, b = map(int, input().split())
    # 计算平均动脉压
    c = (a - b) / 3 + b
    # 输出结果
    print(c)

if __name__ == '__main__':
    main()