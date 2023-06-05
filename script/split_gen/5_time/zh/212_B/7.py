def main():
    # 读入数据
    input_line = input()
    # 解析数据
    x1 = int(input_line[0])
    x2 = int(input_line[1])
    x3 = int(input_line[2])
    x4 = int(input_line[3])
    # 逻辑处理
    if (x1 == x2 and x2 == x3 and x3 == x4):
        print("Weak")
    elif ((x2 == (x1 + 1) % 10) and (x3 == (x2 + 1) % 10) and (x4 == (x3 + 1) % 10)):
        print("Weak")
    else:
        print("Strong")
