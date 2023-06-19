def main():
    # 读取输入
    line = input()
    # 分割输入
    D, T, S = line.split()
    # 转换为数字
    D = int(D)
    T = int(T)
    S = int(S)
    # 计算
    if D <= T * S:
        print("Yes")
    else:
        print("No")
    return
