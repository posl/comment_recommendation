def get_char_list(str):
    char_list = []
    for i in range(len(str)):
        if str[i] not in char_list:
            char_list.append(str[i])
    return char_list

if __name__ == '__main__':
    get_char_list()