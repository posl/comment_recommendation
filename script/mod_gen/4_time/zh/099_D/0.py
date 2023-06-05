def get_input():
    input_list = []
    i = 0
    while True:
        try:
            input_list.append(raw_input())
            i = i + 1
        except EOFError:
            break
    return input_list

if __name__ == '__main__':
    get_input()