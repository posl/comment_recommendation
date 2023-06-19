def main():
    # 读取输入
    line = input()
    # 将输入按空格分割成列表
    line = line.split()
    # 将输入的每个元素转换为整数
    line = [int(x) for x in line]
    # 将输入的每个元素分别赋值给A、B、C
    A, B, C = line[0], line[1], line[2]
    # 计算pow(A,C)和pow(B,C)，并比较大小
    if pow(A, C) > pow(B, C):
        print('>')
    elif pow(A, C) < pow(B, C):
        print('<')
    else:
        print('=')
