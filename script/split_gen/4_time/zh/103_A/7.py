def main():
    # 读取输入
    a1, a2, a3 = map(int, input().split())
    # 三种情况，a1, a2, a3 作为最小值
    # a1 作为最小值
    min_cost = abs(a2 - a1) + abs(a3 - a1)
    # a2 作为最小值
    min_cost = min(min_cost, abs(a1 - a2) + abs(a3 - a2))
    # a3 作为最小值
    min_cost = min(min_cost, abs(a1 - a3) + abs(a2 - a3))
    # 打印结果
    print(min_cost)
