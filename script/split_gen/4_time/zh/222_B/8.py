def get_input():
    input_list = []
    while True:
        try:
            line = input()
            if line == "":
                break
            else:
                input_list.append(line)
        except EOFError:
            break
    return input_list
