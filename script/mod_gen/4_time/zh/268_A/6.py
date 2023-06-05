def main():
    # 读取输入
    input_str = input()
    str_list = input_str.split(' ')
    int_list = [int(str) for str in str_list]
    # 去重
    int_set = set(int_list)
    # 输出
    print(len(int_set))

if __name__ == '__main__':
    main()