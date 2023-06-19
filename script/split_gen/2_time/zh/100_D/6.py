def maxvalue(n, m, cake):
    # n: 蛋糕种类数
    # m: 要吃的蛋糕数
    # cake: 蛋糕的美丽、美味、受欢迎度
    # 返回最大值
    cake.sort(key=lambda x: abs(x[0]) + abs(x[1]) + abs(x[2]), reverse=True)
    # 先按照综合排序
    # 然后按照美丽度排序
    cake.sort(key=lambda x: abs(x[0]), reverse=True)
    # 然后按照美味度排序
    cake.sort(key=lambda x: abs(x[1]), reverse=True)
    # 然后按照受欢迎度排序
    cake.sort(key=lambda x: abs(x[2]), reverse=True)
    # 然后按照综合排序
    # 然后按照美丽度排序
    # 然后按照美味度排序
    # 然后按照受欢迎度排序
    # 以上都是降序排列
    # 第一种蛋糕的综合值最大
    # 在综合值相同的情况下，美丽度最大
    # 在美丽度相同的情况下，美味度最大
    # 在美味度相同的情况下，受欢迎度最大
    # 在受欢迎度相同的情况下，蛋糕的种类最大
    # 以上就是排序的规则
    # 排序完成之后，选择前m个蛋糕的综合值
    # 返回
    result = 0
    for i in range(m):
        result += abs(cake[i][0]) + abs(cake[i][1]) + abs(cake[i][2])
    return result
