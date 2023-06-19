def main():
    # 读取输入
    a,b,c = map(int, input().split())
    # 计算最多能转移多少水
    max_water = a - b
    # 如果2号瓶的水量小于等于最多能转移的水量
    if c <= max_water:
        # 2号瓶的水量为0
        c = 0
    # 否则
    else:
        # 2号瓶的水量为2号瓶的水量减去最多能转移的水量
        c = c - max_water
    # 打印2号瓶的水量
    print(c)
