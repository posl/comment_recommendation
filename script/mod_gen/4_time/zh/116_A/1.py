def main():
    # 读入数据
    a,b,c = map(int, input().split())
    # 计算面积
    s = a * b / 2
    # 输出结果
    print(int(s))

if __name__ == '__main__':
    main()