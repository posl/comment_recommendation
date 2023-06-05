def main():
    # 读取输入
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()
    # 处理
    if u == s:
        a -= 1
    elif u == t:
        b -= 1
    # 输出结果
    print(a, b)

if __name__ == '__main__':
    main()