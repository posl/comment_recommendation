def main():
    # 读取输入
    s = input()
    # 用一个字典记录每个字符出现的次数
    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1
    # 如果只有两种字符，并且每种字符都出现了两次，则打印Yes
    if len(count) == 2 and all([count[c] == 2 for c in count]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()