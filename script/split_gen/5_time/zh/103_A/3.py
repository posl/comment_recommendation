def main():
    # 读入数据
    a = list(map(int, input().split()))
    # 初始化
    cost = 0
    # 从小到大排序
    a.sort()
    # 求出平均值
    mean = sum(a) / len(a)
    # 求出中位数
    median = a[1]
    # 求出最小值
    minimum = a[0]
    # 求出最大值
    maximum = a[2]
    # 求出最小总成本
    cost = maximum - minimum
    # 输出结果
    print(cost)
