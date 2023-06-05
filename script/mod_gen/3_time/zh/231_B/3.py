def main():
    # 读取输入
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # 计算结果
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    # 输出结果
    print(max(d, key=d.get))

if __name__ == '__main__':
    main()