def main():
    # 读取输入
    a = list(map(int, input().split()))
    # 从小到大排序
    a.sort()
    # 计算最小总成本
    ans = a[2] - a[0]
    # 输出答案
    print(ans)
