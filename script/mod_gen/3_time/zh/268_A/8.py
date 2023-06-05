def main():
    # 读入
    input_str = input()
    # 处理
    input_list = input_str.split(" ")
    input_list = list(map(int, input_list))
    input_set = set(input_list)
    # 输出
    print(len(input_set))

if __name__ == '__main__':
    main()