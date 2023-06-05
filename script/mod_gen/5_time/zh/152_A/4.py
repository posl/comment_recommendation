def get_input():
    input_str = input("请输入N M: ")
    input_str_list = input_str.split()
    input_list = [int(x) for x in input_str_list]
    return input_list

if __name__ == '__main__':
    get_input()