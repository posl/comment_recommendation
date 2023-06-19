def get_input():
    input_data = input()
    input_data = input_data.split()
    input_data = [int(x) for x in input_data]
    return input_data

if __name__ == '__main__':
    get_input()