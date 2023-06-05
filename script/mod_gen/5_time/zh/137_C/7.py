def get_char_num(s):
    char_num = [0] * 26
    for char in s:
        char_num[ord(char)-ord('a')] += 1
    return char_num

if __name__ == '__main__':
    get_char_num()