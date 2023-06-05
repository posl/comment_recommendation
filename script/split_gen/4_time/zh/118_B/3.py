def get_input():
    input_list = []
    while True:
        try:
            input_list.append(input())
        except EOFError:
            break
    return input_list
