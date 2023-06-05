def main():
    # 请在此添加代码，实现问题解决方案
    s = input()
    # print(s)
    # print(len(s))
    # print(s[0])
    # print(s[1])
    # print(s[2])
    if len(s) == 3:
        if s[0] == s[1] and s[1] == s[2]:
            print(1)
        elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            print(3)
        else:
            print(6)
    else:
        print("字符串长度不为3")

if __name__ == '__main__':
    main()