def read_input():
    try:
        while True:
            yield input()
    except EOFError:
        pass
