def get_num_of_word(a, b):
    if a == 0 or b == 0:
        return 1
    return get_num_of_word(a-1, b) + get_num_of_word(a, b-1)

if __name__ == '__main__':
    get_num_of_word()