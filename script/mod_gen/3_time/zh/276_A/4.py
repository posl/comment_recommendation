def last_index_of_a(s):
    index = -1
    for i, c in enumerate(s):
        if c == 'a':
            index = i + 1
    return index

if __name__ == '__main__':
    last_index_of_a()