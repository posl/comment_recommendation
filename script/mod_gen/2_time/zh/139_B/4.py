def main():
    # 读取输入
    S = input()
    T = input()
    # 初始化计数器
    count = 0
    # 逐个比较S和T的字符
    for i in range(len(S)):
        if S[i] == T[i]:
            count += 1
    # 输出结果
    print(count)

if __name__ == '__main__':
    main()