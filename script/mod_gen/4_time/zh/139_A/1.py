def main():
    # 读取输入
    S = input()
    T = input()
    # 初始化计数器
    count = 0
    # 遍历字符串
    for i in range(len(S)):
        if S[i] == T[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()