def main():
    # 读入字符串
    S = input()
    # 计数
    count = 0
    # 长度
    length = 0
    # 遍历字符串
    for i in range(len(S)):
        # 如果是ACGT的话
        if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
            # 计数加一
            count += 1
            # 如果长度小于计数的话
            if length < count:
                # 长度等于计数
                length = count
        # 如果不是ACGT的话
        else:
            # 计数等于0
            count = 0
    # 输出长度
    print(length)

if __name__ == '__main__':
    main()