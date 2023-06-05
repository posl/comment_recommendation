def main():
    # 读取输入
    x = input()
    # 处理输入
    x = x.split(" ")
    x = [int(i) for i in x]
    # 处理输出
    print(x.index(0)+1)
