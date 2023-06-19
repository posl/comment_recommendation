def main():
    # 读取输入
    num, height = map(int, input().split())
    heights = list(map(int, input().split()))
    # 计算
    count = 0
    for h in heights:
        if h >= height:
            count += 1
    # 打印结果
    print(count)
