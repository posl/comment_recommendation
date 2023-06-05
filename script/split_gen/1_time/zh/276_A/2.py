def last_index_of_a(text):
    index = -1
    for i in range(len(text)):
        if text[i] == 'a':
            index = i + 1
    return index
