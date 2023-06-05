def get_input():
    input_str = input("请输入两个数，以空格分隔:")
    input_list = input_str.split(" ")
    return input_list

if __name__ == '__main__':
    get_input()