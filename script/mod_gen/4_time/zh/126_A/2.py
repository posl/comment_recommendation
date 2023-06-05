def replace_str_char(str_text, index=0, char=''):
    str_list = list(str_text)
    str_list[index] = char
    return ''.join(str_list)

if __name__ == '__main__':
    replace_str_char()