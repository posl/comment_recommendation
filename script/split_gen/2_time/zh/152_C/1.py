def main():
    # 读取输入
    input_line = input()
    a, b = map(int, input_line.split())
    # 求解并输出
    if a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)
