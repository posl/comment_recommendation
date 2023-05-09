def get_input():
    # Get the input
    input = ''
    try:
        while True:
            input += raw_input()
    except EOFError:
        pass
    # Convert the input to integers
    input = input.split()
    input = [int(i) for i in input]
    return input

if __name__ == '__main__':
    get_input()