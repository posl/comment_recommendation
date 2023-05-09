def get_input_lines():
    while True:
        try:
            line = input()
            yield line
        except EOFError:
            break

if __name__ == '__main__':
    get_input_lines()