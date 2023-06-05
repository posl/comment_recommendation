def main():
    # 读取输入
    line = input()
    # 用空格分割输入
    a, b, c, d = line.split()
    # 将输入转换为整数
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    # 用循环模拟游戏
    while True:
        # 高桥的回合
        c = c - b
        # 如果青木输了，就打印是
        if c <= 0:
            print("是")
            break
        # 青木的回合
        a = a - d
        # 如果高桥输了，就打印否
        if a <= 0:
            print("否")
            break
