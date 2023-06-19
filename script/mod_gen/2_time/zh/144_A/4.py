def main():
    # 读取输入
    s = input().split(" ")
    a = int(s[0])
    b = int(s[1])
    # 输出结果
    if a <= 9 and b <= 9:
        print(a * b)
    else:
        print(-1)

if __name__ == '__main__':
    main()