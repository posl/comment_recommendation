def get_char_list(str):
    char_list = []
    for i in range(0, 26):
        char_list.append(0)
    for i in range(0, len(str)):
        char_list[ord(str[i]) - ord('a')] += 1
    return char_list

if __name__ == '__main__':
    get_char_list()