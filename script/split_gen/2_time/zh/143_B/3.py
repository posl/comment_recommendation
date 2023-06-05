def main():
    # 读取输入
    A, B = map(int, input().split())
    # 计算并打印答案
    print(max(0, A - 2 * B))
