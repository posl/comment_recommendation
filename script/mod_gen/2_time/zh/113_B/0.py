def main():
    # 读入输入
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    # 计算温度
    temp = [t - x * 0.006 for x in h]
    # 找到最接近的温度
    temp = [abs(x - a) for x in temp]
    # 打印结果
    print(temp.index(min(temp)) + 1)
    return

if __name__ == '__main__':
    main()