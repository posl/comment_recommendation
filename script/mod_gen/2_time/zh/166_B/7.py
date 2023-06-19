def main():
    # 读入数据
    n, k = map(int, input().split())
    d = []
    for _ in range(k):
        d.append(int(input()))
        d.extend(list(map(int, input().split())))
    # print(n, k, d)
    # 初始值
    snuke = []
    for i in range(n):
        snuke.append(i + 1)
    # print(snuke)
    # 遍历
    for i in range(k):
        for j in range(d[i]):
            if snuke[j] == d[i + 1 + j]:
                snuke[j] = 0
    # print(snuke)
    # 输出
    print(snuke.count(0))

if __name__ == '__main__':
    main()