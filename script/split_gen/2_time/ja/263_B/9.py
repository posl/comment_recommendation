def get_input_lines():
    while True:
        try:
            line = input()
            yield line
        except EOFError:
            break
