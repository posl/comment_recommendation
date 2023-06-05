def get_char(n,x):
    char_list = []
    for i in range(65,91):
        char_list.append(chr(i)*n)
    char_str = ''.join(char_list)
    return char_str[x-1]

if __name__ == '__main__':
    get_char()