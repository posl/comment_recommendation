def main():
    # 从标准输入中读取字符串
    s = input()
    # 将字符串的第一个字符移到末尾
    s = s[1:] + s[0]
    # 打印结果
    print(s)

if __name__ == '__main__':
    main()