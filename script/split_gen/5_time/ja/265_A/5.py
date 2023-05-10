def get_input_lines():
    while True:
        line = input()
        if line:
            yield line
        else:
            break
