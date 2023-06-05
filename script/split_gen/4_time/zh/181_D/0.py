def solve():
    # 读入数据
    s = input()
    # 生成一个长度为10的数组，记录s中每个数字出现的次数
    count = [0] * 10
    for c in s:
        count[int(c)] += 1
    # 从8开始，每次加8，判断是否可以用s中的数字组成
    for i in range(8, 1000, 8):
        # 生成一个长度为10的数组，记录i中每个数字出现的次数
        c = [0] * 10
        for j in str(i):
            c[int(j)] += 1
        # 如果i中的数字可以用s中的数字组成，打印"是"
        if all([count[k] >= c[k] for k in range(10)]):
            print("是")
            return
    # 如果i中的数字不可以用s中的数字组成，打印"否"
    print("否")
