def get_input():
    input = raw_input()
    input = input.split(" ")
    input = [int(x) for x in input]
    return input
