def main():
    # 读入数据
    n, k = map(int, input().split())
    # 零食的种类
    d = []
    # 零食的编号
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    # 零食的种类
    # print(d)
    # 零食的编号
    # print(a)
    # 零食的编号集合
    a_set = set()
    for i in range(k):
        for j in range(d[i]):
            a_set.add(a[i][j])
    # print(a_set)
    # 受害者的数量
    count = 0
    for i in range(1, n+1):
        if i not in a_set:
            count += 1
    print(count)

if __name__ == '__main__':
    main()