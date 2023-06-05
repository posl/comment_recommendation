def main():
    # 读取输入
    a, b, c = map(int, input().split())
    # 从瓶子2转移到瓶子1
    b += c
    # 2号瓶中还会有多少水？
    print(b if b < a else a)
