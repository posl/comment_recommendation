def get_input():
    input_list = []
    while True:
        input_data = input()
        if input_data == "":
            break
        input_list.append(input_data)
    return input_list
