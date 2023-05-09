def get_input():
    input_list = []
    input_list.append(int(input()))
    for i in range(input_list[0]):
        input_list.append(list(map(int, input().split())))
    return input_list

if __name__ == '__main__':
    get_input()