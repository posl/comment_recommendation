def find_last_index_of_a(string):
    string_length = len(string)
    if string_length < 1 or string_length > 100:
        return -1
    for i in range(string_length, 0, -1):
        if string[i-1] == 'a':
            return i
    return -1
