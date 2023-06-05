def swap(str, a, b):
    str_list = list(str)
    str_list[a-1], str_list[b-1] = str_list[b-1], str_list[a-1]
    return ''.join(str_list)

if __name__ == '__main__':
    swap()