def main():
    # 读入数据
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    # print(data)
    # 定义一个空列表，用于存储最终的输出结果
    result = []
    # 定义一个空列表，用于存储袋子里的球
    bag = []
    # 循环读取每一行数据
    for i in range(n):
        # 判断当前行的第一个数字是1, 2, 还是3
        if data[i][0] == 1:
            # 如果是1，则在袋子里放入一个新的球
            bag.append(data[i][1])
        elif data[i][0] == 2:
            # 如果是2，则将袋子里的每个球的数字都加上当前行的第二个数字
            for j in range(len(bag)):
                bag[j] += data[i][1]
        elif data[i][0] == 3:
            # 如果是3，则将袋子里的最小的数字取出来
            # 并将取出来的数字放入result列表中
            # 并从袋子里删除这个数字
            result.append(min(bag))
            bag.remove(min(bag))
    # print(result)
    # 循环输出result列表中的数字
    for i in range(len(result)):
        print(result[i])
