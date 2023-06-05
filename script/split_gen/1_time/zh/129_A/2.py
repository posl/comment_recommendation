def main():
    # 获取输入
    p, q, r = map(int, input().split())
    # 计算最小时间
    min_time = p + q
    if min_time > q + r:
        min_time = q + r
    if min_time > r + p:
        min_time = r + p
    # 打印结果
    print(min_time)
