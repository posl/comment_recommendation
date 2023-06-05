def main():
    # 读取输入
    line = input()
    # 用空格分割输入
    s = line.split()
    # 将输入转换为整数
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    # 计算答案
    ans = a + b + c
    # 打印答案
    print(ans)
