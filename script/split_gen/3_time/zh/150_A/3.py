def main():
    # 读取输入
    inputs = input()
    # 分割字符串
    inputs = inputs.split()
    # 转换为整数
    k = int(inputs[0])
    x = int(inputs[1])
    # 判断
    if k * 500 >= x:
        print("是")
    else:
        print("否")
