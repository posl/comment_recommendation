def get_input():
    input_list = []
    while True:
        try:
            input_list.append(list(map(int, input().split())))
        except EOFError:
            break
    return input_list

if __name__ == '__main__':
    get_input()