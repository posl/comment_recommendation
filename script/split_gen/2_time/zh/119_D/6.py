def get_input():
    input = []
    while True:
        try:
            input.append(raw_input())
        except EOFError:
            break
    return input
