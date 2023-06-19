def main():
    # 读取输入
    line1 = input().split()
    n = int(line1[0])
    m = int(line1[1])
    x = int(line1[2])
    # print(n, m, x)
    # 读取书的信息
    books = []
    for i in range(n):
        line = input().split()
        books.append([int(line[0]), list(map(int, line[1:]))])
    # print(books)
    # 用于记录最小的花费
    min_cost = -1
    # 遍历所有的书的组合
    for i in range(1, 2 ** n):
        # 用于记录当前组合的总花费
        cost = 0
        # 用于记录当前组合对每个算法的理解水平
        understand = [0] * m
        # 遍历每本书
        for j in range(n):
            # 如果当前书在当前组合中
            if i & (1 << j):
                cost += books[j][0]
                for k in range(m):
                    understand[k] += books[j][1][k]
        # 判断当前组合是否满足要求
        if min(understand) >= x:
            # 如果当前组合满足要求，更新最小花费
            if min_cost == -1:
                min_cost = cost
            else:
                min_cost = min(min_cost, cost)
    print(min_cost)

if __name__ == '__main__':
    main()