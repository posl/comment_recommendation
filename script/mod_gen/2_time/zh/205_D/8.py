def get_input():
    input_str = input()
    input_str = input_str.split()
    input = [int(input_str[0]), int(input_str[1]), int(input_str[2])]
    return input

if __name__ == '__main__':
    get_input()