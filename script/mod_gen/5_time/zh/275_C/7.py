def read_input():
    try:
        while True:
            yield input()
    except EOFError:
        pass

if __name__ == '__main__':
    read_input()