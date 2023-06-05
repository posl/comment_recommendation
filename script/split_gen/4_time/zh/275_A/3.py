def main():
    # 读取输入
    n = int(input())
    h = list(map(int, input().split()))
    # 计算并打印结果
    print(h.index(max(h)) + 1)
