def get_input():
    input_list = []
    while True:
        try:
            line = input()
            input_list.append(line)
        except EOFError:
            break
    return input_list

if __name__ == '__main__':
    get_input()