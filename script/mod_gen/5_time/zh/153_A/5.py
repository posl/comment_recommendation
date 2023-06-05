def get_input():
    input = raw_input()
    input = input.split(" ")
    input = [int(x) for x in input]
    return input

if __name__ == '__main__':
    get_input()