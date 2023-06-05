def reverse_string(string, start, end):
    string_list = list(string)
    string_list[start:end+1] = reversed(string_list[start:end+1])
    return ''.join(string_list)

if __name__ == '__main__':
    reverse_string()