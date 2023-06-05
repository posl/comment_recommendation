def main():
    # 输入
    s = input()
    # 8的倍数的数字的个数
    count = 0
    # 遍历数字序列s
    for i in range(len(s)):
        # 如果是8的倍数
        if int(s[i]) % 8 == 0:
            count += 1
    # 如果8的倍数的数字的个数大于0
    if count > 0:
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    main()