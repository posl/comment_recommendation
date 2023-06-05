def main():
    # 读入字符串
    s = input()
    # 用set来存储排列组合后的字符串
    s_set = set()
    # 遍历s的所有排列组合
    for i in range(len(s)):
        for j in range(len(s)):
            for k in range(len(s)):
                s_set.add(s[i] + s[j] + s[k])
    # 输出set的大小
    print(len(s_set))

if __name__ == '__main__':
    main()