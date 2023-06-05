def main():
    # 读取输入
    a, b = map(int, input().split())
    # 处理
    a_str = str(a) * b
    b_str = str(b) * a
    # 输出
    if a_str < b_str:
        print(a_str)
    else:
        print(b_str)
