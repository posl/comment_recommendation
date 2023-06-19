def main():
    # 读取输入
    input_line = input()
    # 用空格分隔输入
    input_line = input_line.split(" ")
    # 创建一个长度为26的列表
    output_list = [0 for i in range(26)]
    # 用循环把输入的数字转换为字母
    for i in range(26):
        output_list[int(input_line[i]) - 1] = chr(i + 97)
    # 把列表转换为字符串
    output_str = "".join(output_list)
    # 输出结果
    print(output_str)
