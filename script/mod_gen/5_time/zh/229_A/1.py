def main():
    # 读入数据
    s1 = input()
    s2 = input()
    # 初始化
    flag = False
    # 处理
    if s1[0] == '#' and s1[1] == '#' and s2[0] == '#' and s2[1] == '#':
        flag = True
    # 输出结果
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()