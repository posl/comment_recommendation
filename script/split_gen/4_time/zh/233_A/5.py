def get_input():
    input_line = input()
    input_line = input_line.split()
    input_line = [int(x) for x in input_line]
    return input_line
