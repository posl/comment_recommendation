def reverse_string(string, start, end):
    string_list = list(string)
    while start < end:
        temp = string_list[start]
        string_list[start] = string_list[end]
        string_list[end] = temp
        start += 1
        end -= 1
    return ''.join(string_list)

if __name__ == '__main__':
    reverse_string()