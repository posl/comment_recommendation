def main():
    # 读取数据
    a, b = map(int, input().split())
    # 计算折扣率
    discount = (a - b) / a * 100
    # 打印结果
    print(discount)
