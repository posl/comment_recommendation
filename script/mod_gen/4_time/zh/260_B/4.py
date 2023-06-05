def get_input():
    input_list = []
    while True:
        try:
            input_list.append(input())
        except:
            break
    return input_list

if __name__ == '__main__':
    get_input()