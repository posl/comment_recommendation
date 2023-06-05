def main():
    # 读取输入
    n, a, b = map(int, input().split())
    # 蓝球数
    blue = 0
    # 蓝球数增加的次数
    count = 0
    # 蓝球数增加的次数限制
    limit = 10 ** 100
    while count < limit:
        # 增加蓝球数
        blue = blue + a
        # 增加蓝球数增加的次数
        count = count + 1
        # 如果增加蓝球数的次数达到限制，跳出循环
        if count == limit:
            break
        # 增加红球数
        blue = blue - b
        # 增加蓝球数增加的次数
        count = count + 1
        # 如果增加蓝球数的次数达到限制，跳出循环
        if count == limit:
            break
    # 打印蓝球数
    print(blue)
