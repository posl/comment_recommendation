def get_input():
    input_str = input()
    input_str_list = input_str.split(" ")
    return {"A":int(input_str_list[0]),"B":int(input_str_list[1])}

if __name__ == '__main__':
    get_input()