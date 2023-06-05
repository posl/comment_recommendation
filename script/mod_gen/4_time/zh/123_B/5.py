def main():
    # 读入数据
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # 计算最后一道菜的最早送达时间
    # 1. 计算所有菜品的最早送达时间
    # 2. 取最大值
    # 3. 按10的倍数取上限
    print(max([((A+9)//10)*10,((B+9)//10)*10,((C+9)//10)*10,((D+9)//10)*10,((E+9)//10)*10]))

if __name__ == '__main__':
    main()