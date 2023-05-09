def get_input_lines():
    while True:
        try:
            yield raw_input()
        except EOFError:
            break
