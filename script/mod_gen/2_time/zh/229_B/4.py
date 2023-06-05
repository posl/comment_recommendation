def main():
    # 读入数据
    S_1 = input()
    S_2 = input()
    # 处理数据
    if S_1[0] == '#' and S_1[1] == '#' and S_2[0] == '#' and S_2[1] == '#':
        print('Yes')
    else:
        print('No')
    # 输出结果

if __name__ == '__main__':
    main()