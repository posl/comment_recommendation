def main():
    # 读取输入
    s = input()
    t = input()
    # 计算结果
    count = 0
    for i in range(3):
        if s[i] == t[i]:
            count += 1
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()