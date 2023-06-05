def get_input():
    input = raw_input()
    input_list = input.split(' ')
    return int(input_list[0]), int(input_list[1]), int(input_list[2])

if __name__ == '__main__':
    get_input()