def main():
    # 读入数据
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    # 依次处理t中的字符
    result = ""
    for c in t:
        if c == "1":
            result += s1
        elif c == "2":
            result += s2
        elif c == "3":
            result += s3
    # 打印结果
    print(result)

if __name__ == '__main__':
    main()