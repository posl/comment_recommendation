def main():
    # 读取输入
    input_str = input()
    # 处理
    if input_str[0] == input_str[1] and input_str[1] == input_str[2]:
        output_str = "Won"
    else:
        output_str = "Lost"
    # 输出
    print(output_str)

if __name__ == '__main__':
    main()