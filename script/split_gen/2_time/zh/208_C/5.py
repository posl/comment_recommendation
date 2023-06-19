def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 对数据进行排序
    a.sort()
    # 求出每人分得的糖果
    # 每人分得的糖果的最小值
    min_candy = k // n
    # 余下的糖果
    remain_candy = k % n
    # 分配糖果
    for i in range(n):
        # 当前分配的糖果数
        candy = min_candy
        if remain_candy > 0:
            candy += 1
            remain_candy -= 1
        # 输出结果
        print(candy)
