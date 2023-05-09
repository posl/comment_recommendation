def get_input_lines():
    while True:
        try:
            yield raw_input()
        except EOFError:
            break

if __name__ == '__main__':
    get_input_lines()