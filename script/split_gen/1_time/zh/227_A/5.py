def main():
    # 读取输入
    input_line = input()
    input_line = input_line.split(" ")
    # print(input_line)
    n = int(input_line[0])
    k = int(input_line[1])
    a = int(input_line[2])
    # print(n, k, a)
    # 开始处理
    # 用一个数组表示每个人的卡片数量
    card_nums = [0 for i in range(n)]
    # print(card_nums)
    # 从a开始发牌，循环k次
    for i in range(k):
        # print(i)
        # print(a)
        # print(card_nums)
        card_nums[a-1] += 1
        # print(card_nums)
        # print("-----")
        a += 1
        if a > n:
            a = 1
    # print(card_nums)
    # 找到最大值
    max_num = max(card_nums)
    # print(max_num)
    # 找到最大值的索引
    max_index = card_nums.index(max_num)
    # print(max_index)
    # print(max_index + 1)
    # 输出结果
    print(max_index + 1)
