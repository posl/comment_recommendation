def main():
    # 读取输入
    A, B, C = map(int, input().split())
    # 从瓶子2转移到瓶子1
    B = B + C
    # 瓶子2中剩余的水
    C = 0
    # 瓶子1中最多可以装多少水
    D = A
    # 瓶子1中剩余的水
    A = A - B
    # 瓶子1中剩余的水
    B = B - D
    # 瓶子2中剩余的水
    C = C + B
    # 输出结果
    print(C)
# 调用主函数
