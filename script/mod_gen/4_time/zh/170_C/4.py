def get_input():
    input_str = raw_input()
    input_list = input_str.split(" ")
    input_list = [int(i) for i in input_list]
    return input_list

if __name__ == '__main__':
    get_input()