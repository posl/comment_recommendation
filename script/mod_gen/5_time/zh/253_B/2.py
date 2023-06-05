def get_input():
    result = []
    while True:
        try:
            line = input()
            result.append(line)
        except EOFError:
            break
    return result

if __name__ == '__main__':
    get_input()