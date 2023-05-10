def swap_char(s,a,b):
    char_list = list(s)
    char_list[a-1], char_list[b-1] = char_list[b-1], char_list[a-1]
    return ''.join(char_list)
