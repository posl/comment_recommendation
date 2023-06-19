def get_input():
    input = raw_input()
    input = input.split(' ')
    input = map(int, input)
    return input

if __name__ == '__main__':
    get_input()