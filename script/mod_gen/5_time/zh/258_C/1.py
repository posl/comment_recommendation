def main():
    # 读取输入
    n, q = map(int, input().split())
    s = input()
    # 以列表形式存储
    s = list(s)
    # 处理查询
    for i in range(q):
        t, x = map(str, input().split())
        x = int(x)
        if t == '1':
            # 1 x:连续执行以下x次：删除S的最后一个字符并将其附加到开头。
            for j in range(x):
                s.insert(0, s.pop())
        elif t == '2':
            # 2 x:打印S的第x个字符。
            print(s[x - 1])

if __name__ == '__main__':
    main()