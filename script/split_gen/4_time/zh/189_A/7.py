def main():
    # 读取输入
    input_str = input()
    # 处理输入
    if input_str[0] == input_str[1] and input_str[1] == input_str[2]:
        # 输出结果
        print('Won')
    else:
        # 输出结果
        print('Lost')
