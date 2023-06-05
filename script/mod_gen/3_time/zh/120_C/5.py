def main():
    # 读入数据
    s = input()
    # 初始化
    red = 0
    blue = 0
    # 计算
    for i in range(len(s)):
        if s[i] == "0":
            red += 1
        else:
            blue += 1
    # 输出
    print(min(red, blue) * 2)

if __name__ == '__main__':
    main()