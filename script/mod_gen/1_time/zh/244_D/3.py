def main():
    # 输入
    s = input().split()
    t = input().split()
    # 处理
    # 输出
    if s[0] == t[0] and s[1] == t[1] and s[2] == t[2]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()