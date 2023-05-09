def replace_word(str, a, b):
    return str[:a-1] + str[b-1] + str[a:b-1] + str[a-1] + str[b:]

if __name__ == '__main__':
    replace_word()