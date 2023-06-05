def main():
    # 读取输入
    s = input()
    # 计算中心字符的位置
    center = int((len(s) + 1) / 2)
    # 打印中心字符
    print(s[center - 1])
