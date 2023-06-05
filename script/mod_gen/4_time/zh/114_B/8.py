def main():
    # 读入数据
    S = input()
    # 计算结果
    min = 1000
    for i in range(0, len(S) - 2):
        X = int(S[i:i + 3])
        if abs(X - 753) < min:
            min = abs(X - 753)
    # 输出结果
    print(min)

if __name__ == '__main__':
    main()