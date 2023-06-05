def main():
    # 读取数据
    n, m = map(int, input().split())
    # print(n, m)
    # 读取第二行开始的m行数据，每行数据的第一个是参加聚会的人数，后面的是参加聚会的人的编号
    data = []
    for i in range(m):
        line = list(map(int, input().split()))
        # print(line)
        # 读取每行数据的第一个是参加聚会的人数，后面的是参加聚会的人的编号
        data.append(line[1:])
    # print(data)
    # 每两个人都至少参加过一次同一个聚会，则打印Yes；否则打印No。
    # 思路：两两比较
    for i in range(n):
        for j in range(n):
            if i != j:
                # print(i, j)
                # print(data[i], data[j])
                # 判断两个列表是否有交集
                if set(data[i]) & set(data[j]) == set():
                    print("No")
                    return
    print("Yes")

if __name__ == '__main__':
    main()