def main():
    # 从标准输入读取
    a1, a2, a3 = map(int, input().split())
    # 计算并打印答案
    print(min(abs(a1 - a2) + abs(a2 - a3), abs(a1 - a3) + abs(a3 - a2), abs(a2 - a1) + abs(a1 - a3)))
