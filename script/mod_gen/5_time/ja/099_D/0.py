def get_input_lines():
    while True:
        try:
            line = input()
            yield line
        except EOFError:
            return

if __name__ == '__main__':
    get_input_lines()