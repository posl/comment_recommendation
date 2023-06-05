def main():
    # 读取数据
    S = input()
    # 计算结果
    if S[-1] == "s":
        print(S + "es")
    else:
        print(S + "s")
