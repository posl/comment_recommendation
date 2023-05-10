def swap(input_string, a, b):
    a = a - 1
    b = b - 1
    input_string_list = list(input_string)
    tmp = input_string_list[a]
    input_string_list[a] = input_string_list[b]
    input_string_list[b] = tmp
    return "".join(input_string_list)

if __name__ == '__main__':
    swap()