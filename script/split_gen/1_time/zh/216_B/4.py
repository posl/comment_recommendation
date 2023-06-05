def get_input():
    input_data = []
    while True:
        try:
            line = input()
            if line == '':
                break
            input_data.append(line)
        except EOFError:
            break
    return input_data
