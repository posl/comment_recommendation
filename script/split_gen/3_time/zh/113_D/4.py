def amidakuji(h, w, k):
    # 1. 生成所有可能的横线
    # 2. 从中选出满足条件的横线
    # 3. 计算满足条件的横线的数量
    # 4. 返回
    # 1. 生成所有可能的横线
    def gen_lines(h, w):
        if h == 0:
            return [[]]
        else:
            lines = gen_lines(h - 1, w)
            return [line + [h] for line in lines if len(line) < w] + \
                   [line for line in lines if len(line) == w]
    # 2. 从中选出满足条件的横线
    def is_valid(line):
        # 1. 没有两条水平线共享一个端点。
        # 2. 每条水平线的两个端点必须在同一高度。
        # 3. 一条水平线必须连接相邻的垂直线。
        return all([len(set(line)) == len(line),
                    len(set(line)) == 2,
                    all([abs(line[i] - line[i + 1]) == 1
                         for i in range(len(line) - 1)])])
    # 3. 计算满足条件的横线的数量
    def count_valid_lines(w):
        return len([line for line in gen_lines(h, w) if is_valid(line)])
    # 4. 返回
    return count_valid_lines(w) % 1000000007
