def get_input():
    input_str = input()
    input_str = input_str.split(' ')
    return int(input_str[0]), int(input_str[1])

if __name__ == '__main__':
    get_input()