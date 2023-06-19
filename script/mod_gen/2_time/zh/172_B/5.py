def main():
    # 输入
    S = input()
    T = input()
    # 计算
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    # 输出
    print(count)

if __name__ == '__main__':
    main()