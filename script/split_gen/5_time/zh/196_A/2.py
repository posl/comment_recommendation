def main():
    # 读取输入
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    # 计算并输出答案
    print(max(a - c, a - d, b - c, b - d))
