def main():
    # 读入三个字符串
    s1 = input()
    s2 = input()
    s3 = input()
    # 读入T
    T = input()
    # 用T中的字符决定输出的字符
    ans = ""
    for i in T:
        if i == "1":
            ans += s1
        elif i == "2":
            ans += s2
        else:
            ans += s3
    # 打印答案
    print(ans)

if __name__ == '__main__':
    main()