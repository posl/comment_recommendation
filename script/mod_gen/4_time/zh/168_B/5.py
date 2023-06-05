def main():
    # 读取输入
    k = int(input())
    s = input()
    # 处理
    if len(s) > k:
        s = s[0:k] + "..."
    # 输出结果
    print(s)

if __name__ == '__main__':
    main()