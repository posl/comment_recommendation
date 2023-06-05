def last_index_of_a(s):
    index = -1
    for i, c in enumerate(s):
        if c == 'a':
            index = i + 1
    return index
