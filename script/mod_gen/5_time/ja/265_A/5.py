def get_input_lines():
    while True:
        line = input()
        if line:
            yield line
        else:
            break

if __name__ == '__main__':
    get_input_lines()