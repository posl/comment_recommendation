def main():
    # 获取输入
    input_line = input()
    # 分割输入
    input_line = input_line.split()
    # 获取第一个数字
    first_num = input_line[0]
    # 获取第二个数字
    second_num = input_line[1]
    # 计算第一个数字的总和
    first_num_sum = 0
    for i in range(len(first_num)):
        first_num_sum += int(first_num[i])
    # 计算第二个数字的总和
    second_num_sum = 0
    for i in range(len(second_num)):
        second_num_sum += int(second_num[i])
    # 输出
    if first_num_sum > second_num_sum:
        print(first_num_sum)
    elif first_num_sum < second_num_sum:
        print(second_num_sum)
    else:
        print(first_num_sum)
