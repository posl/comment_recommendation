def main():
    # 读入数据
    s = input()
    # 计算中心字符的位置
    pos = (len(s) + 1) // 2
    # 打印中心字符
    print(s[pos - 1])

if __name__ == '__main__':
    main()