def main():
    # 读取输入
    a, b = input().split()
    # 计算
    a = int(a)
    b = int(b)
    a_str = str(a)
    b_str = str(b)
    a_str *= b
    b_str *= a
    if a_str < b_str:
        print(a_str)
    else:
        print(b_str)
    return
